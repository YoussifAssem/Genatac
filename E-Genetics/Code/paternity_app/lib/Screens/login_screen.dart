// ignore_for_file: camel_case_types, use_key_in_widget_constructors

import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';
import 'package:paternity_app/Screens/menu.dart';
import 'package:paternity_app/Screens/signup_screen.dart';

class logIn extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _logIn();
  }
}

class _logIn extends State<logIn> {
  final email = TextEditingController();
  final password = TextEditingController();
  User user = User();
  late String text;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Scaffold(
        backgroundColor: const Color.fromARGB(255, 209, 207, 207),
        appBar: AppBar(
          automaticallyImplyLeading: false,
          backgroundColor: Colors.blue[900],
          title: const Text(
            'Log In',
            style: TextStyle(color: Colors.white),
          ),
        ),
        body: ListView(
          children: [
            const SizedBox(
              height: 40,
            ),
            const Center(
              child: Text(
                'Welcome In Genetics',
                style: TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                    fontStyle: FontStyle.italic,
                    fontSize: 30),
              ),
            ),
            const SizedBox(height: 20),
            Center(
              child: ElevatedButton(
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.blue[900]),
                ),
                child: const Text('Sign Up Here'),
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => SignUp()),
                  );
                },
              ),
            ),
            const SizedBox(
              height: 50,
            ),
            TextFormField(
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 18,
                color: Colors.white,
              ),
              keyboardType: TextInputType.emailAddress,
              controller: email,
              decoration: InputDecoration(
                border: const OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(15.0)),
                  borderSide: BorderSide.none,
                ),
                filled: true,
                fillColor: Colors.blue[900],
                hintText: 'Email',
                hintStyle: const TextStyle(fontSize: 18, color: Colors.white),
              ),
            ),
            const SizedBox(
              height: 50,
            ),
            TextFormField(
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 18,
                color: Colors.white,
              ),
              //keyboardType: TextInputType.visiblePassword,
              controller: password,
              decoration: InputDecoration(
                border: const OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(15.0)),
                  borderSide: BorderSide.none,
                ),
                filled: true,
                fillColor: Colors.blue[900],
                hintText: 'Password',
                hintStyle: const TextStyle(fontSize: 18, color: Colors.white),
              ),
              obscureText: true,
            ),
            const SizedBox(height: 50),
            SizedBox(
                height: 45,
                child: Padding(
                  padding: const EdgeInsets.only(left: 250),
                  child: ElevatedButton(
                    style: ButtonStyle(
                      backgroundColor:
                          MaterialStateProperty.all(Colors.blue[900]),
                    ),
                    child: const Text('Log In'),
                    onPressed: () async {
                      if (email.text == '' || password.text == '') {
                        text = 'Error, Please fill all requirements';
                        showAlertDialog(context);
                      } else if (!email.text.contains('@')) {
                        text = 'Email format is not true';
                        showAlertDialog(context);
                      } else {
                        if (await user.login(email.text, password.text) ==
                            'Error') {
                          text = 'Error, Email or Password is incorrect';
                          showAlertDialog(context);
                        } else {
                          Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => Menu()),
                          );
                        }
                      }
                    },
                  ),
                ))
          ],
        ),
      ),
    );
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
