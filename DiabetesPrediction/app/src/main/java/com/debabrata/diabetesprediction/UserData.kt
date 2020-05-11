package com.debabrata.diabetesprediction
import com.google.gson.annotations.SerializedName

data class UserData (
        @SerializedName("preg") val preg : String,
        @SerializedName("plas") val plas : String,
        @SerializedName("pres") val pres : String,
        @SerializedName("skin") val skin : String,
        @SerializedName("test") val test : String,
        @SerializedName("mass") val mass : String,
        @SerializedName("pedi") val pedi : String,
        @SerializedName("age") val age : String
)
