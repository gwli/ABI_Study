/*
 * Copyright (C) 2009 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package dd.ee.cc;

import android.app.Activity;
import android.widget.TextView;
import android.os.Bundle;

/*
 * This class loads the Java Native Interface (JNI) conformant library
 * 'libAndroid2.so' and provides an access to exported C functions.
 * The library is packaged into and installed with the application's APK.
 * The native method is implemented in the C file /jni/Android2.c file
 * 
 * For more information on JNI, see: http://java.sun.com/docs/books/jni/
 */

public class Android2 extends Activity
{
    private TextView tv;
    
    /* Called on Activity creation. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);

        /* Create a TextView and set its content.
         * the text is returned by the native method called via JNI.
         */
        tv = new TextView(this);
        tv.setText( "Starting..." );
        setContentView(tv);
        
        Thread updateThread = new Thread(new Runnable() {
            public void run() {
                while (true) {
                    tv.post(new Runnable() {
                        public void run() {
                            tv.setText( stringFromJNI() );
                        }
                    });
                    try { Thread.sleep(1000); } catch (Exception e) { }
                    tv.post(new Runnable() {
                        public void run() {
                            tv.setText("");
                        }
                    });
                    try { Thread.sleep(1000); } catch (Exception e) { }
                }
            }
        });
        updateThread.start();
        
    }

    /*
     * An example native method. See the library function
     * <code>Java_dd_ee_cc_Android2_stringFromJNI</code>
     * for the implementation details.
     */
    public native String stringFromJNI();

    /* This is another native method declaration that is *not*
     * implemented by 'Android2'. It demonstrates that
     * you can declare as many native methods in your Java code
     * as you wish to, because a method's implementation is searched
     * in the native libraries loaded into an application's process
     * only at the first time the Java code calls it.
     *
     * Trying to call this method will result in an
     * java.lang.UnsatisfiedLinkError exception!
     */
    public native String  unimplementedJNIMethod();

    /* This is the static constructor used to load the
     * 'Android2' library when the class is
     * loaded.
     */
    static { System.loadLibrary("Android2"); }
}
