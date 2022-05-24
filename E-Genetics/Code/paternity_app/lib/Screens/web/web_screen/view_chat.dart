// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';
import 'package:paternity_app/Screens/splash_screen.dart';
import 'package:paternity_app/Screens/web/web_screen/chat_screen.dart';

import 'menu.dart';

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
      drawer: Menu(),
      backgroundColor: const Color.fromARGB(255, 38, 54, 80),
      appBar: AppBar(
        backgroundColor: const Color.fromARGB(255, 38, 54, 80),
        title: const Text(
          'Admin Users',
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
              //child: Text("There Are a problem in the system"),
              child: Splash(),
            );
          }
          return ListView(
            children: snapshot.data!.docs.map((doc) {
              return Column(
                  children: [
                const SizedBox(height: 10),
                Container(
                  padding: const EdgeInsets.only(top: 10, bottom: 10),      
                  margin: const EdgeInsets.only(right: 10, left: 10,),
                  decoration: const BoxDecoration(
                    borderRadius: BorderRadius.all(Radius.circular(10)),
                    color: Colors.white,
                  ),
                  child: ListTile(
                   leading: const CircleAvatar(radius: 30,
                   backgroundImage: AssetImage("images/contact.png"),
                    ),
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
                          color: Colors.black),
                    ),
                  ),
                ),
                const SizedBox(height: 0),
              ].toList());
            }).toList(),
          );
        },
      ),
    );
  }
}
