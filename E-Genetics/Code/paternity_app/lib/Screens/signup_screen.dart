import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:paternity_app/Models/user.dart';
import 'package:paternity_app/Screens/login_screen.dart';

// ignore: use_key_in_widget_constructors
class SignUp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _SignUp();
  }
}

class _SignUp extends State<SignUp> {
  // ignore: unused_field

  User user = User();
  final name = TextEditingController();
  final e = TextEditingController();
  final p = TextEditingController();
  final cP = TextEditingController();

  String text = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromARGB(255, 209, 207, 207),
        appBar: AppBar(
          backgroundColor: Colors.blue[900],
          title: const Text(
            'Sign Up',
            style: TextStyle(color: Colors.white),
          ),
        ),
        body: Padding(
            padding: const EdgeInsets.all(2),
            child: ListView(children: <Widget>[
              const SizedBox(height: 50),
              const Center(
                  child: Text(
                'Sign Up',
                style: TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                    fontStyle: FontStyle.italic,
                    fontSize: 30),
              )),
              const SizedBox(height: 25),
              TextFormField(
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 18,
                  color: Colors.white,
                ),
                keyboardType: TextInputType.emailAddress,
                controller: name,
                inputFormatters: <TextInputFormatter>[
                  FilteringTextInputFormatter.deny(RegExp('[^a-zA-Z]')),
                ],
                decoration: InputDecoration(
                  border: const OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(15.0)),
                    borderSide: BorderSide.none,
                  ),
                  filled: true,
                  fillColor: Colors.blue[900],
                  hintText: 'Name',
                  hintStyle: const TextStyle(fontSize: 18, color: Colors.white),
                ),
              ),
              const SizedBox(height: 25.0),
              TextFormField(
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 18, color: Colors.white),
                keyboardType: TextInputType.emailAddress,
                controller: e,
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
                height: 25.0,
              ),
              TextFormField(
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 18, color: Colors.white),
                //keyboardType: TextInputType.visiblePassword,
                controller: p,
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
              const SizedBox(
                height: 25.0,
              ),
              TextFormField(
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 18, color: Colors.white),
                controller: cP,
                decoration: InputDecoration(
                  border: const OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(15.0)),
                    borderSide: BorderSide.none,
                  ),
                  filled: true,
                  fillColor: Colors.blue[900],
                  hintText: 'Confirm Password',
                  hintStyle: const TextStyle(fontSize: 18, color: Colors.white),
                ),
                obscureText: true,
              ),
              const SizedBox(
                height: 25.0,
              ),
              SizedBox(
                height: 50,
                child: Padding(
                  padding: const EdgeInsets.only(left: 250),
                  child: ElevatedButton(
                    child: const Text(
                      'Sign Up',
                    ),
                    style: ButtonStyle(
                      backgroundColor:
                          MaterialStateProperty.all(Colors.blue[900]),
                    ),
                    onPressed: () async => {
                      if (name.text == '' ||
                          e.text == '' ||
                          p.text == '' ||
                          cP.text == '')
                        {
                          text = 'Error, Please fill all requirements',
                          showAlertDialog(context),
                        }
                      else if (p.text != cP.text)
                        {
                          text = 'Error, Password does not match',
                          showAlertDialog(context),
                        }
                      else if (!e.text.contains('@'))
                        {
                          text = 'Email format is not applicable',
                          showAlertDialog(context),
                        }
                      else if (p.text.length <= 6)
                        {
                          text = ' Weak Password !',
                          showAlertDialog(context),
                        }
                      else
                        {
                          if (await user.signUp(
                                  name: name.text,
                                  email: e.text,
                                  password: p.text) ==
                              'Error')
                            {
                              text =
                                  'Error Email is Aleady Exist OR There are an error in Data',
                              showAlertDialog(context),
                            }
                          else
                            {
                              Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (context) => logIn()),
                              )
                            }
                        }
                    },
                  ),
                ),
              )
            ])));
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
