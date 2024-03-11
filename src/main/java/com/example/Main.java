package com.example;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Size;
import org.opencv.videoio.VideoCapture;
import org.opencv.videoio.VideoWriter;
import org.opencv.videoio.Videoio;

public class Main {
    
    static { System.loadLibrary(Core.NATIVE_LIBRARY_NAME); }

    public static void main(String[] args) {
        System.out.println("Hello world!");

        VideoCapture cap1 = new VideoCapture("video1.mp4");
        VideoCapture cap2 = new VideoCapture("video2.mp4");

        Size frameSize = new Size((int) cap1.get(Videoio.CAP_PROP_FRAME_WIDTH),
                                  (int) cap1.get(Videoio.CAP_PROP_FRAME_HEIGHT));
        int fourcc = VideoWriter.fourcc('X', 'V', 'I', 'D');
        VideoWriter writer = new VideoWriter("merged_vide1.avi", fourcc, cap1.get(Videoio.CAP_PROP_FPS),
                                             frameSize, true);

        Mat frame = new Mat();

        // Merge video1
        while (cap1.read(frame)) {
            writer.write(frame);
        }

        // Merge video2
        while (cap2.read(frame)) {
            writer.write(frame);
        }

        cap1.release();
        cap2.release();
        writer.release();
    }
}