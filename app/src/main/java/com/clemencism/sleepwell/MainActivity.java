package com.clemencism.sleepwell;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.os.Bundle;



public class MainActivity extends AppCompatActivity {

    private String[] images = {"drawable/beautiful_cascade_environment_460621.jpg"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ConstraintLayout layout =(ConstraintLayout)findViewById(R.id.mainLayout);
        layout.setBackgroundResource(R.drawable.);
    }
}
