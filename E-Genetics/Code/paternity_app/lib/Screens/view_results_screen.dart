// ignore_for_file: use_key_in_widget_constructors, camel_case_types, prefer_initializing_formals, must_be_immutable

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class viewResults extends StatefulWidget {
  late String _userName;
  late String _caseID;

  viewResults({required String userName, required String caseID}) {
    _userName = userName;
    _caseID = caseID;
  }
  @override
  State<StatefulWidget> createState() {
    // ignore: no_logic_in_create_state
    return _viewResults(userName: _userName, caseID: _caseID);
  }
}

class _viewResults extends State<viewResults> {
  late String _userName;
  late String _caseID;

  _viewResults({required String userName, required String caseID}) {
    _userName = userName;
    _caseID = caseID;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.blueGrey[900],
        appBar: AppBar(
          backgroundColor: Colors.blue[900],
          title: const Text(
            'Results',
          ),
          actions: [
            Container(
              alignment: Alignment.centerRight,
              child: Text(
                FirebaseAuth.instance.currentUser!.email.toString(),
                style: const TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                    fontStyle: FontStyle.italic),
              ),
            )
          ],
        ),
        body: StreamBuilder<QuerySnapshot>(
          stream: FirebaseFirestore.instance
              .collection('adminUsers')
              .doc(_userName)
              .collection('Results')
              .where('ID', isEqualTo: _caseID)
              .snapshots(),
          builder:
              (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
            if (!snapshot.hasData) {
              return const Center(
                child: Text(
                  "\t\t\t\t\t\t\tAdmin Name You Entered Is Not True \n May be Admin Not Submit the data until now",
                  style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.bold),
                ),
              );
            }
            return ListView(
              children: snapshot.data!.docs.map((doc) {
                return Column(
                    children: [
                  const SizedBox(height: 50),
                  const Text(
                    '\t\t\t\t\t\tProbability of Child \n that related to this Father',
                    style: TextStyle(
                        fontSize: 30,
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.bold,
                        color: Colors.green),
                  ),
                  const SizedBox(height: 30),
                  Container(
                    margin: const EdgeInsets.only(right: 20, left: 20),
                    decoration: const BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.circular(30)),
                      color: Colors.green,
                    ),
                    child: ListTile(
                      title: Text(
                        doc['probabilityFather'].toString(),
                        textAlign: TextAlign.center,
                        style: const TextStyle(
                            fontWeight: FontWeight.bold, fontSize: 25),
                      ),
                    ),
                  ),
                  const SizedBox(height: 80),
                  const Text(
                    '\t\t\t\t\t\t\t\t\tProbability of Child \n that Not related to this Father',
                    style: TextStyle(
                        fontSize: 30,
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.bold,
                        color: Colors.red),
                  ),
                  const SizedBox(height: 30),
                  Container(
                    margin: const EdgeInsets.only(right: 20, left: 20),
                    decoration: const BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.circular(30)),
                      color: Colors.red,
                    ),
                    child: ListTile(
                      title: Text(
                        doc['probabilityNotFather'].toString(),
                        textAlign: TextAlign.center,
                        style: const TextStyle(
                            fontWeight: FontWeight.bold, fontSize: 25),
                      ),
                    ),
                  ),
                ].toList());
              }).toList(),
            );
          },
        ));
  }
}
