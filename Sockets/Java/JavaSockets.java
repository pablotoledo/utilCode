/*
@jpablotoledo

Send a binary file over client socket in Java

*/
package javasockets;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;

/**
*
* @author jpablotoledo
*/
public class JavaSockets {

    public static void main(String[] args) throws IOException {
		//Create a new socket object
        Socket socket = new Socket("localhost",5500);
		//Configure the socket to work with a buffer stream
        BufferedOutputStream bufferWrite = new BufferedOutputStream(socket.getOutputStream());
		//Create a file object
        File file = new File("location of your file");
        //Buffer for read the file
		FileInputStream in = new FileInputStream(file);
         int len;
        byte flujo[] = new byte[1024];
        while ((len = in.read(flujo)) > 0) {
            bufferWrite.write(flujo, 0, len);
        }
        //Close connection
        in.close();
        bufferWrite.close();
        socket.close();
		
    }
    
}
