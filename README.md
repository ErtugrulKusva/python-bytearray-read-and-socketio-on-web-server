# python bytearray serial reading example and integration with flask socketio on web server
 *There are 2 programs.

*The task of the Arduino side is to generate random data, place them in a certain array(gonData) and send this data over the serial.

*The task of the Python side is to read the random data and transfer it to an empty array. Elements placed in this array are printed on the web server with using socketio.

*You must install the relevant libraries to run the programs

Process of the program

[English]

This program has been written with using threading, socketio, serial reading, flask pyhton libraries.

The flow of the program is hierarchically given below.

1)Defining libraries

2)Starting async mode

3)setuping web server

4)Installing socket on the web server

5)starting threading

6)Reading data from serial port and converting to list and transfering into empty array

7)Decoding and transferring data which is transferred into array.

8)Sending the data to web server

9)showing data on web interface(I used html-css-js)

Programın akışı

[Türkçe]

Bu program python programlama dilinin threading, socketio, serial port okuma,flask, kütüphanelerinin kullanımını öğretmek amacıyla yazılmıştır.

Programın çalışması hiyerarşik olarak aşağıda verilmiştir.

1)Kütüphanelerin tanıtılması

2)Asyn modun açılması- serial read, web server, socketionun eş zamanlı çalışmasını sağlar.

3)Web server kurulumu

4)Socketionun web server üzerine kurulması

5)Threadingin açılması(paralel işlem yapma)

6)Seri porttan gelen verilerin okunması daha sonra liste dönüştürülüp arraye aktarılması

7)Arraye aktarılmış byte yapısındaki verilerin çözümlenmesi(decode edilmesi) ve değişkenlere aktarılması

8)Değişkenlere aktarılan verilerin socketio ile web server üzerine gönderilmesi

9)Web serverin gelen verileri arayüzde görünür hale getirilmesi
