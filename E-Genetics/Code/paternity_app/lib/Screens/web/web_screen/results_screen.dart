// ignore_for_file: use_key_in_widget_constructors, camel_case_types, avoid_print

import 'dart:convert';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:crypto/crypto.dart';
import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';
import 'package:paternity_app/Screens/web/web_screen/view_results_screen.dart';

class Results extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _Results();
  }
}

class _Results extends State<Results> {
  final caseID = TextEditingController();
  final userName = TextEditingController();
  final nationalID = TextEditingController();

  late String text;
  User user = User();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromARGB(255, 209, 207, 207),
        appBar: AppBar(
          automaticallyImplyLeading: false,
          backgroundColor: Colors.blue[900],
          title: const Text(
            'Results',
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
        body: ListView(children: [
          Container(
              padding: const EdgeInsets.only(left: 400, top: 25, right: 400),
              child: GestureDetector(
                  onTap: () {
                    FocusScope.of(context).unfocus();
                  },
                  child: Column(
                    children: [
                      const SizedBox(
                        height: 80,
                      ),
                      Center(
                        child: TextFormField(
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            fontSize: 18,
                            color: Colors.white,
                          ),
                          controller: userName,
                          decoration: InputDecoration(
                            border: const OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15.0)),
                              borderSide: BorderSide.none,
                            ),
                            filled: true,
                            fillColor: Colors.blue[900],
                            hintText: 'Enter Admin User Name',
                            hintStyle: const TextStyle(
                                fontSize: 18, color: Colors.white),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 50,
                      ),
                      Center(
                        child: TextFormField(
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            fontSize: 18,
                            color: Colors.white,
                          ),
                          controller: caseID,
                          decoration: InputDecoration(
                            border: const OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15.0)),
                              borderSide: BorderSide.none,
                            ),
                            filled: true,
                            fillColor: Colors.blue[900],
                            hintText: 'Enter Case Number',
                            hintStyle: const TextStyle(
                                fontSize: 18, color: Colors.white),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 50,
                      ),
                      Center(
                        child: TextFormField(
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            fontSize: 18,
                            color: Colors.white,
                          ),
                          controller: nationalID,
                          maxLength: 14,
                          decoration: InputDecoration(
                            border: const OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15.0)),
                              borderSide: BorderSide.none,
                            ),
                            filled: true,
                            fillColor: Colors.blue[900],
                            hintText: 'Enter National ID',
                            hintStyle: const TextStyle(
                                fontSize: 18, color: Colors.white),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 50,
                      ),
                      Center(
                        child: ElevatedButton(
                            style: ButtonStyle(
                              backgroundColor:
                                  MaterialStateProperty.all(Colors.blue[900]),
                            ),
                            child: const Text('View Results'),
                            onPressed: () async {
                              if (caseID.text == '' || userName.text == '') {
                                text = 'Error, Please fill all requirements';
                                showAlertDialog(context);
                              } else if (nationalID.text.length != 14) {
                                text = 'Error, Ntional ID is Not Exist';
                                showAlertDialog(context);
                              } else {
                                try {
                                  DocumentReference ref = FirebaseFirestore
                                      .instance
                                      .collection('adminUsers')
                                      .doc(userName.text)
                                      .collection('Results')
                                      .doc(sha256
                                          .convert(utf8.encode(nationalID.text))
                                          .toString());
                                  FirebaseFirestore.instance
                                      .runTransaction((transaction) async {
                                    DocumentSnapshot snapShot =
                                        await transaction.get(ref);
                                    if (snapShot.exists) {
                                      if (snapShot['ID'] ==
                                              sha256
                                                  .convert(utf8
                                                      .encode(nationalID.text))
                                                  .toString() &&
                                          snapShot['caseNumber'] ==
                                              sha256
                                                  .convert(
                                                      utf8.encode(caseID.text))
                                                  .toString()) {
                                        Navigator.push(
                                          context,
                                          MaterialPageRoute(
                                              builder: (context) => viewResults(
                                                    userName: userName.text,
                                                    caseNumber: sha256
                                                        .convert(utf8.encode(
                                                            caseID.text))
                                                        .toString(),
                                                    nationalID: sha256
                                                        .convert(utf8.encode(
                                                            nationalID.text))
                                                        .toString(),
                                                  )),
                                        );
                                      } else {
                                        text = 'Error, Data Is Not Exist';
                                        showAlertDialog(context);
                                      }
                                    } else {
                                      text = 'Error, User Name Is Not Exist';
                                      showAlertDialog(context);
                                    }
                                  });
                                } catch (e) {
                                  text = 'Error, Exception error occured';
                                  showAlertDialog(context);
                                }
                              }
                            }),
                      ),
                    ],
                  )))
        ]));
  }

  showAlertDialog(
    BuildContext context,
  ) {
    // Create button
    Widget okButton = TextButton(
      child: const Text("OK"),
      onPressed: () {
        Navigator.of(context).pop();
      },
    );

    // Create AlertDialog
    AlertDialog alert = AlertDialog(
      title: const Text("Alert"),
      content: Text(text),
      actions: [
        okButton,
      ],
    );

    // show the dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }
}
