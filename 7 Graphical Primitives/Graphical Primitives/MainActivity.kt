package com.example.graphicalprimitives

import android.annotation.SuppressLint
import android.app.Activity
import android.content.Context
import android.graphics.*
import android.os.Bundle
import android.view.View

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val customDrawingView = CustomDrawingView(this)
        setContentView(customDrawingView)
    }
}

class CustomDrawingView(context: Context) : View(context) {
    private val shapePaint = Paint()
    private val textPaint = Paint()
    init {
        shapePaint.isAntiAlias = true
        shapePaint.style = Paint.Style.FILL
        textPaint.isAntiAlias = true
        textPaint.color = Color.BLACK
        textPaint.textSize = 60f
    }
    @SuppressLint("DrawAllocation")
    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        canvas.drawColor(Color.WHITE)
        val screenWidth = width.toFloat()
        val screenHeight = height.toFloat()
        val shapes = mutableListOf<Pair<Path, Paint>>()
        val rectanglePath = Path()
        rectanglePath.addRect(0f, 0f, screenWidth, screenHeight, Path.Direction.CW)
        shapes.add(Pair(rectanglePath, Paint().apply { color = Color.GREEN }))
        val trianglePath = Path()
        trianglePath.moveTo(screenWidth / 2, 0f)
        trianglePath.lineTo(0f, screenHeight)
        trianglePath.lineTo(screenWidth, screenHeight)
        trianglePath.close()
        shapes.add(Pair(trianglePath, Paint().apply { color = Color.RED }))
        for ((path, paint) in shapes) {
            canvas.drawPath(path, paint)
        }
        canvas.drawText("Hello there!!!", 360f, 700f, textPaint)
    }
}