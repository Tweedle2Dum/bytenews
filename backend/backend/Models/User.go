package models

type User struct {
	Email string `gorm:"type:varchar(200);primary_key;not_null"`
}
