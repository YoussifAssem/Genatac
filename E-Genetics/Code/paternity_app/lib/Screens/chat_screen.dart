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
      body: ListView(
        children: [
          const SizedBox(height: 50),
          Center(
            child: Text(
              _title,
              style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                  fontStyle: FontStyle.italic,
                  fontSize: 30),
            ),
          ),
          const SizedBox(height: 80),
          Container(
              margin: const EdgeInsets.only(left: 50),
              child: Row(
                children: [
                  Table(
                    defaultColumnWidth: const FixedColumnWidth(160.0),
                    border: TableBorder.all(style: BorderStyle.none),
                    children: [
                      TableRow(children: [
                        Column(
                          children: const [
                            Text(
                              'Father',
                              style: TextStyle(
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                                fontSize: 25,
                                fontStyle: FontStyle.italic,
                              ),
                            ),
                          ],
                        ),
                        Column(
                          children: const [
                            Text(
                              'Mother',
                              style: TextStyle(
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                                fontSize: 25,
                                fontStyle: FontStyle.italic,
                              ),
                            ),
                          ],
                        ),
                      ]),
                      TableRow(children: [
                        Column(
                          children: [
                            Container(
                              margin: const EdgeInsets.only(right: 20),
                              child: TextFormField(
                                maxLength: 1,
                                textCapitalization:
                                    TextCapitalization.sentences,
                                inputFormatters: [
                                  FilteringTextInputFormatter.allow(
                                      RegExp("[A-T-C-G]")),
                                ],
                                textAlign: TextAlign.center,
                                style: const TextStyle(
                                  fontSize: 18,
                                  color: Colors.white,
                                ),
                                controller: father1,
                                decoration: InputDecoration(
                                  border: const OutlineInputBorder(
                                    borderRadius:
                                        BorderRadius.all(Radius.circular(15.0)),
                                    borderSide: BorderSide.none,
                                  ),
                                  filled: true,
                                  fillColor: Colors.blue[900],
                                  hintText: 'Allele 1',
                                  hintStyle: const TextStyle(
                                    fontSize: 18,
                                  ),
                                ),
                              ),
                            ),
                            const SizedBox(height: 20),
                            Container(
                              margin: const EdgeInsets.only(right: 20),
                              child: TextFormField(
                                inputFormatters: [
                                  FilteringTextInputFormatter.allow(
                                      RegExp("[A-T-C-G]")),
                                ],
                                textCapitalization:
                                    TextCapitalization.sentences,
                                maxLength: 1,
                                textAlign: TextAlign.center,
                                style: const TextStyle(
                                  fontSize: 18,
                                  color: Colors.white,
                                ),
                                controller: father2,
                                decoration: InputDecoration(
                                  border: const OutlineInputBorder(
                                    borderRadius:
                                        BorderRadius.all(Radius.circular(15.0)),
                                    borderSide: BorderSide.none,
                                  ),
                                  filled: true,
                                  fillColor: Colors.blue[900],
                                  hintText: 'Allele 2',
                                  hintStyle: const TextStyle(
                                    fontSize: 18,
                                  ),
                                ),
                              ),
                            )
                          ],
                        ),
                        Column(
                          children: [
                            Container(
                              margin: const EdgeInsets.only(left: 20),
                              child: TextFormField(
                                inputFormatters: [
                                  FilteringTextInputFormatter.allow(
                                      RegExp("[A-T-C-G]")),
                                ],
                                textCapitalization:
                                    TextCapitalization.sentences,
                                maxLength: 1,
                                textAlign: TextAlign.center,
                                style: const TextStyle(
                                  fontSize: 18,
                                  color: Colors.white,
                                ),
                                controller: mother1,
                                decoration: InputDecoration(
                                  border: const OutlineInputBorder(
                                    borderRadius:
                                        BorderRadius.all(Radius.circular(15.0)),
                                    borderSide: BorderSide.none,
                                  ),
                                  filled: true,
                                  fillColor: Colors.blue[900],
                                  hintText: 'Allele 1',
                                  hintStyle: const TextStyle(
                                    fontSize: 18,
                                  ),
                                ),
                              ),
                            ),
                            const SizedBox(height: 20),
                            Container(
                              margin: const EdgeInsets.only(left: 20),
                              child: TextFormField(
                                inputFormatters: [
                                  FilteringTextInputFormatter.allow(
                                      RegExp("[A-T-C-G]")),
                                ],
                                textCapitalization:
                                    TextCapitalization.sentences,
                                maxLength: 1,
                                textAlign: TextAlign.center,
                                style: const TextStyle(
                                  fontSize: 18,
                                  color: Colors.white,
                                ),
                                controller: mother2,
                                decoration: InputDecoration(
                                  border: const OutlineInputBorder(
                                    borderRadius:
                                        BorderRadius.all(Radius.circular(15.0)),
                                    borderSide: BorderSide.none,
                                  ),
                                  filled: true,
                                  fillColor: Colors.blue[900],
                                  hintText: 'Allele 2',
                                  hintStyle: const TextStyle(
                                    fontSize: 18,
                                  ),
                                ),
                              ),
                            )
                          ],
                        ),
                      ]),
                    ],
                  )
                ],
              )),
          const SizedBox(height: 50),
          Container(
            margin: const EdgeInsets.only(left: 200),
            child: ElevatedButton(
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.blue[900]),
                ),
                onPressed: () {},
                child: const Text(
                  'Results',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                    fontSize: 18,
                    fontStyle: FontStyle.italic,
                  ),
                )),
          )
        ],
      ),
    );
  }
}
