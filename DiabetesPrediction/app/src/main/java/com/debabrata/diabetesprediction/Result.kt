package com.debabrata.diabetesprediction

import android.app.DownloadManager
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Layout
import android.view.View
import android.widget.RelativeLayout
import kotlin.random.Random

class Result : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)
        setResult("data")

    }
    fun setResult(data: String){
        val uri : Uri = Uri.parse("pythonanywhere.com")
    }

}
