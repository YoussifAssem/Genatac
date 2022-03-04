// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';

class viewChat extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _viewChat();
  }
}

class _viewChat extends State<viewChat> {
  final search = TextEditingController();
  User user = User();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[900],
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue[900],
        title: const Text(
          'View Chatting',
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
      //body:
    );
  }
}
