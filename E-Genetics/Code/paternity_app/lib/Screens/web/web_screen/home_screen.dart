// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';
import 'menu.dart';

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
        drawer: Menu(),
        backgroundColor: const Color.fromARGB(255, 209, 207, 207),
        appBar: AppBar(
          backgroundColor: Colors.blue[900],
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
            image: AssetImage("images/family-law.png"),
          )),
          /* child: const TextField(
              decoration:
                 // InputDecoration(fillColor: Colors.green, filled: true),
            )*/
        ));
  }
}
