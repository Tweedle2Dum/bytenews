package main

import (
	models "backend/Models"
	"log"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
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
	//db_key := os.Getenv("DB_KEY")
	db, err := gorm.Open(postgres.Open(os.Getenv("DB_KEY")+"&application_name=$ docs_simplecrud_gorm"), &gorm.Config{}) //gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{})
	if err != nil {
		log.Fatal(err)
	}

	db.AutoMigrate(&models.User{})

	r := gin.Default()
	r.Use(CORSMiddleware())
	r.POST("/create", func(c *gin.Context) {
		var user models.User
		err := c.BindJSON(&user)
		if err != nil {
			c.JSON(400, gin.H{
				"message": "error",
				"data":    err.Error(),
			})
			return
		}
		db.Create(&models.User{Email: user.Email})
		c.JSON(201, gin.H{
			"message": "success",
			"data":    user,
		})
	})
	r.GET("/read", func(c *gin.Context) {
		var users []models.User
		db.Find(&users)
		c.JSON(200, gin.H{
			"message": "success",
			"data":    users,
		})
	})
	r.DELETE("/delete/:id", func(c *gin.Context) {
		var user models.User
		log.Println(c.Param("id"))
		db.Where("Email=?", c.Param("id")).Delete(&models.User{})
		c.JSON(200, gin.H{
			"message": "success",
			"data":    user,
		})
	})
	r.Run() // listen and serve on
}
