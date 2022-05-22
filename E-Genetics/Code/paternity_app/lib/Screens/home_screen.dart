// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';

class homeScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _homeScreen();
  }
}

class _homeScreen extends State<homeScreen> {
  User user = User();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromARGB(255, 38, 54, 80),
        appBar: AppBar(
          backgroundColor: const Color.fromARGB(255, 38, 54, 80),
          title: const Text(
            'Home Page',
          ),
          actions: [
            Container(
              alignment: Alignment.centerRight,
              child: Text(
                user.Email,
                style: const TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                    fontStyle: FontStyle.italic),
              ),
            )
          ],
        ),
        body: Container(
          constraints: const BoxConstraints.expand(),
          decoration: const BoxDecoration(
              image: DecorationImage(
                  image: AssetImage("Images/d7ka4.png"),
                  fit: BoxFit.cover)),
          /* child: const TextField(
              decoration:
                 // InputDecoration(fillColor: Colors.green, filled: true),
            )*/
        ));
  }
}
