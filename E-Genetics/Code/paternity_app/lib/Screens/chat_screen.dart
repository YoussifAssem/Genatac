// ignore_for_file: must_be_immutable, no_logic_in_create_state, unused_field, prefer_final_fields, use_key_in_widget_constructors

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:paternity_app/Models/user.dart';

class Chat extends StatefulWidget {
  late String _title;
  Chat(String title) {
    _title = title;
  }
  @override
  State<StatefulWidget> createState() {
    return _Chat(_title);
  }
}

class _Chat extends State<Chat> {
  late String _title;
  User _user = User();
  final father1 = TextEditingController();
  final father2 = TextEditingController();
  final mother1 = TextEditingController();
  final mother2 = TextEditingController();

  _Chat(String title) {
    _title = title;
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[900],
      appBar: AppBar(
        backgroundColor: Colors.blue[900],
        title: Text(
          _title,
        ),
        actions: [
          Container(
            alignment: Alignment.centerRight,
            child: Text(
              _user.Email,
              style: const TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                  fontStyle: FontStyle.italic),
            ),
          )
        ],
      ),
      // body:
    );
  }
}
