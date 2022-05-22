// ignore_for_file: use_key_in_widget_constructors, camel_case_types, prefer_initializing_formals, must_be_immutable

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class viewResults extends StatefulWidget {
  late String _userName;
  late String _nationalID;
  late String _caseNumber;

  viewResults(
      {required String userName,
      required String nationalID,
      required String caseNumber}) {
    _userName = userName;
    _nationalID = nationalID;
    _caseNumber = caseNumber;
  }
  @override
  State<StatefulWidget> createState() {
    // ignore: no_logic_in_create_state
    return _viewResults(
        userName: _userName, nationalID: _nationalID, caseNumber: _caseNumber);
  }
}

class _viewResults extends State<viewResults> {
  late String _userName;
  late String _nationalID;
  late String _caseNumber;

  _viewResults(
      {required String userName,
      required String nationalID,
      required String caseNumber}) {
    _userName = userName;
    _nationalID = nationalID;
    _caseNumber = caseNumber;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromARGB(255, 38, 54, 80),
        appBar: AppBar(
          backgroundColor: const Color.fromARGB(255, 38, 54, 80),
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
              .where('ID', isEqualTo: _nationalID)
              .where('caseNumber', isEqualTo: _caseNumber)
              .snapshots(),
          builder:
              (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
            if (!snapshot.hasData) {
              return const Center(
                child: Text(
                  "\t\t\t\t\t\t\tAdmin Name You Entered Is Not True \n May be Admin Not Submit the data until now",
                  style: TextStyle(
                      color: Colors.black,
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
                        color: Colors.white),
                  ),
                  const SizedBox(height: 30),
                  Container(
                    margin: const EdgeInsets.only(right: 20, left: 20),
                    decoration: const BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.circular(30)),
                      color: Colors.white,
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
                    '\t\t\t\t\tProbability of Child \n that Not related to this \n Father',
                    style: TextStyle(
                        fontSize: 30,
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.bold,
                        color: Colors.white),
                  ),
                  const SizedBox(height: 30),
                  Container(
                    margin: const EdgeInsets.only(right: 20, left: 20),
                    decoration: const BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.circular(30)),
                      color: Colors.white,
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
                  const SizedBox(height: 80),
                  Text(
                    doc['result'],
                    style: const TextStyle(
                        fontSize: 23,
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.bold,
                        color: Colors.black),
                  ),
                ].toList());
              }).toList(),
            );
          },
        ));
  }

  bool checkProbability(double probFather, double probNotFather) {
    if (probFather > probNotFather) {
      return true;
    } else {
      return false;
    }
  }
}
