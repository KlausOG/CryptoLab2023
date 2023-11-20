package com.example.animations

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.view.animation.AnimationUtils
import android.widget.Button
import android.widget.ImageView

class MainActivity : AppCompatActivity() {
    private lateinit var imageView: ImageView
    private lateinit var blinkButton: Button
    private lateinit var rotateButton: Button
    private lateinit var fadeButton: Button
    private lateinit var moveButton: Button
    private lateinit var slideButton: Button
    private lateinit var zoomButton: Button
    private lateinit var stopButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        imageView = findViewById(R.id.imageview)
        blinkButton = findViewById(R.id.ButtonBlink)
        rotateButton = findViewById(R.id.ButtonRotate)
        fadeButton = findViewById(R.id.ButtonFade)
        moveButton = findViewById(R.id.ButtonMove)
        slideButton = findViewById(R.id.ButtonSlide)
        zoomButton = findViewById(R.id.ButtonZoom)
        stopButton = findViewById(R.id.ButtonStop)

        blinkButton.setOnClickListener(View.OnClickListener {
            imageView.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.blink))
        })

        rotateButton.setOnClickListener(View.OnClickListener {
            imageView.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.rotate))
        })

        fadeButton.setOnClickListener(View.OnClickListener {
            imageView.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.fade))
        })

        moveButton.setOnClickListener(View.OnClickListener {
            imageView.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.move))
        })

        slideButton.setOnClickListener(View.OnClickListener {
            imageView.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.slide))
        })

        zoomButton.setOnClickListener(View.OnClickListener {
            imageView.startAnimation(AnimationUtils.loadAnimation(applicationContext, R.anim.zoom))
        })

        stopButton.setOnClickListener(View.OnClickListener {
            imageView.clearAnimation()
        })
    }
}