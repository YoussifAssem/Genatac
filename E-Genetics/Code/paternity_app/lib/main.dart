// ignore_for_file: use_key_in_widget_constructors
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
//TO RUN WEB REMOVE THESES
//import 'Screens/web/web_screen/splash_screen.dart';
//import 'Screens/web/web_screen/login_screen.dart';

//MOBILE SCREENS
import 'Screens/splash_screen.dart';
import 'Screens/login_screen.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  //To Run Mobile App remove this comment and run
  await Firebase.initializeApp();
//To Run Web App PLEASE if you will run the web RUN WITHOUT DEBUGGING remove this comment and run
/*
  await Firebase.initializeApp(
      options: const FirebaseOptions(
    apiKey: "AIzaSyCmuZGl5AWSah3INjLhA7fpZhXXMMtT1wk",
    appId: "1:86992490246:web:8d547713d9626cbed1d887",
    messagingSenderId: "86992490246",
    projectId: "paternitytest-7cb8b",
  ));
*/
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitUp,
      DeviceOrientation.portraitDown,
      DeviceOrientation.landscapeRight,
      DeviceOrientation.landscapeLeft,
    ]);
    return MaterialApp(
      // Log In For mobile

      routes: {
        '/logIn': (context) => logIn(),
      },
      home: const Splash(),
    );

    //Log In For web
    /*
      routes: {
        '/logIn': (context) => logIn(),
      },
      home: const Splash(),
    );
    */
  }
}
