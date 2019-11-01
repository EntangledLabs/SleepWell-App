package com.clemencism.sleepwell;


import android.content.Context;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;

import org.opencv.android.CameraBridgeViewBase;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.face.*;

public class GetTiredness {



    public static void main(String[] args) {
        String filePath = "images/4/image4.png";
        CascadeClassifier faceCascade = new CascadeClassifier();



        String casadePath = "cascades/data/haarcascade_frontalface_alt2.xml";
        faceCascade.load(casadePath);

        Imgcodecs imageCodecs = new Imgcodecs();
        Mat img = imageCodecs.imread(filePath);

        Mat imggray = new Mat();
        Imgproc.cvtColor(img, imggray, Imgproc.COLOR_BGR2GRAY);

        MatOfRect faces = new MatOfRect();
        faceCascade.detectMultiScale(imggray, faces, 1.2, 6);

        LBPHFaceRecognizer faceRecognizer = LBPHFaceRecognizer.create();
        faceRecognizer.read("./recognizers/face-trainner.yml");


    }


}



