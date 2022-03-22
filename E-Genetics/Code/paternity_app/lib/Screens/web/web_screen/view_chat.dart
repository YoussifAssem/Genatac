// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';
import 'package:paternity_app/Screens/chat_screen.dart';

class viewChat extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _viewChat();
  }
}

class _viewChat extends State<viewChat> {
  User user = User();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 209, 207, 207),
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue[900],
        title: const Text(
          'View Users',
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
      body: StreamBuilder<QuerySnapshot>(
        stream: FirebaseFirestore.instance.collection('adminUsers').snapshots(),
        builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
          if (!snapshot.hasData) {
            return const Center(
              child: Text("There Are a problem in the system"),
            );
          }
          return ListView(
            children: snapshot.data!.docs.map((doc) {
              return Column(
                  children: [
                const SizedBox(height: 50),
                Container(
                  margin: const EdgeInsets.only(right: 400, left: 400),
                  decoration: BoxDecoration(
                    borderRadius: const BorderRadius.all(Radius.circular(30)),
                    color: Colors.blue[900],
                  ),
                  child: ListTile(
                    onTap: () {
                      Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => Chat(doc['userName'])));
                    },
                    title: Text(
                      doc['userName'].toString(),
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 25,
                          color: Colors.white),
                    ),
                  ),
                ),
                const SizedBox(height: 30),
              ].toList());
            }).toList(),
          );
        },
      ),
    );
  }
}
