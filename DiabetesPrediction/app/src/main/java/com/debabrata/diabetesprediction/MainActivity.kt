package com.debabrata.diabetesprediction

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.view.View
import android.widget.EditText
import android.widget.ProgressBar
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.gson.Gson


class MainActivity : AppCompatActivity() {

    private val handler :Handler = Handler()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val intent = Intent(this, Result::class.java).apply{
            putExtra("com.debabrata.diabetesprediction", "message")
        }



    }
    /** Called when the user taps the Send button */
    fun sendMessage(view: View) {
        var jsonObject = buildJsonObject()
        Toast.makeText(applicationContext, jsonObject!!, Toast.LENGTH_LONG).show()

        // Do something in response to button
        val progressBar = findViewById<ProgressBar>(R.id.loading)
        progressBar.visibility = View.VISIBLE
        var i: Int
        var j= 0
        i = progressBar!!.progress
        //run the progress bar thread
        Thread(Runnable {while (j < 15){
            while (i < 100) {
                i += 5
                // Update the progress bar and display the current value
                handler.post {
                    progressBar.progress = i
                }
                try {
                    Thread.sleep(100)
                } catch (e: InterruptedException) {
                    e.printStackTrace()
                }

            }
            j += 1
        }

        })
        handler.postDelayed(Runnable {
            val intent = Intent(this, Result::class.java).apply{
//                name, message
                putExtra("com.debabrata.diabetesprediction.jsonObject", "message")
            }
            progressBar.visibility = View.GONE
            startActivity(intent)},5000)


    }
    fun buildJsonObject(): String? {
        var preg = findViewById<EditText>(R.id.preg).text.toString()
        var plas = findViewById<EditText>(R.id.plas).text.toString()
        var pres = findViewById<EditText>(R.id.pres).text.toString()
        var skin = findViewById<EditText>(R.id.skin).text.toString()
        var test = findViewById<EditText>(R.id.test).text.toString()
        var mass = findViewById<EditText>(R.id.mass).text.toString()
        var pedi = findViewById<EditText>(R.id.pedi).text.toString()
        var age = findViewById<EditText>(R.id.age).text.toString()

        var user_data = UserData(preg,plas,pres,skin,test,mass,pedi,age)
        val gson = Gson()
        var outputJson = gson.toJson(user_data)
        return outputJson

    }

}
