// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'dart:convert';

import 'package:crypto/crypto.dart';
import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';
import 'package:paternity_app/Screens/view_results_screen.dart';

class Results extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _Results();
  }
}

class _Results extends State<Results> {
  final caseID = TextEditingController();
  final userName = TextEditingController();

  late String text;
  User user = User();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.blueGrey[900],
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
        body: ListView(
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
                    borderRadius: BorderRadius.all(Radius.circular(15.0)),
                    borderSide: BorderSide.none,
                  ),
                  filled: true,
                  fillColor: Colors.blue[900],
                  hintText: 'Enter Admin User Name',
                  hintStyle: const TextStyle(fontSize: 18, color: Colors.white),
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
                    borderRadius: BorderRadius.all(Radius.circular(15.0)),
                    borderSide: BorderSide.none,
                  ),
                  filled: true,
                  fillColor: Colors.blue[900],
                  hintText: 'Enter Case Number',
                  hintStyle: const TextStyle(fontSize: 18, color: Colors.white),
                ),
              ),
            ),
            const SizedBox(
              height: 50,
            ),
            Center(
              child: ElevatedButton(
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.blue[900]),
                ),
                child: const Text('View Results'),
                onPressed: () async {
                  if (caseID.text == '' || userName.text == '') {
                    text = 'Error, Please fill all requirements';
                    showAlertDialog(context);
                  } else {
                    var digest1 = sha256
                        .convert(utf8.encode(caseID.text)); // Hashing Process
                    print("Digest as hex string: $digest1");

                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => viewResults(
                                userName: userName.text,
                                caseID:
                                    '876bd08d2e46b02bfd07438c84d316f7c0ea50a38d582898d0c5b0a3430be640',
                              )),
                    );
                  }
                },
              ),
            ),
          ],
        ));
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
