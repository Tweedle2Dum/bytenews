package main

import (
	models "backend/Models"
	"context"
	"log"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"github.com/mailgun/mailgun-go/v3"
)

func CORSMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {

		c.Header("Access-Control-Allow-Origin", "*")
		c.Header("Access-Control-Allow-Credentials", "true")
		c.Header("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT, DELETE")

		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(204)
			return
		}

		c.Next()
	}
}
func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	if err != nil {
		log.Fatal(err)
	}

	r := gin.Default()
	r.Use(CORSMiddleware())
	r.POST("/create", func(c *gin.Context) {
		var user models.User
		if err := c.ShouldBindJSON(&user); err != nil {
			c.JSON(400, gin.H{"error": err.Error()})
			return
		}
		c.BindJSON(&user)
		mg := mailgun.NewMailgun("https://api.mailgun.net/v3/lists/daily@daily.bytesizenewsletter.tech/members", os.Getenv("MAILGUN_API_KEY"))

		member := mailgun.Member{
			Address: user.Email,
		}
		ctx, cancel := context.WithTimeout(context.Background(), time.Second*30)
		defer cancel()
		err := mg.CreateMember(ctx, true, "daily@daily.bytesizenewsletter.tech", member)
		if err != nil {
			log.Fatal(err)
			c.JSON(400, gin.H{"error": err.Error()})
			return
		}
		c.JSON(201, gin.H{"message": "success"})

	})
	r.Run() // listen and serve on
}
