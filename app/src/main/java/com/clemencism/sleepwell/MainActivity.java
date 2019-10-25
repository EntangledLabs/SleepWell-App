package com.clemencism.sleepwell;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.os.Bundle;



public class MainActivity extends AppCompatActivity {

    private int[] images = {R.drawable.background1, R.drawable.background2, R.drawable.background3, R.drawable.background4};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ConstraintLayout layout =(ConstraintLayout)findViewById(R.id.mainLayout);
        int index = (int)Math.random()*3;
        layout.setBackgroundResource(images[index]);
    }
}
