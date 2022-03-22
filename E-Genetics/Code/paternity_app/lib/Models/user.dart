// ignore_for_file: non_constant_identifier_names, body_might_complete_normally_nullable

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

class User {
  // ignore: prefer_final_fields, unused_field
  late String _name;
  late String _email;
  late String _password;

  signUp({
    required String name,
    required String email,
    required String password,
  }) async {
    try {
      _setName(name);
      _setEmail(email);
      _setPassword(password);
      if (getEmail() != 'Error' &&
          getName() != 'Error' &&
          getPassword() != 'Error') {
        final list =
            await FirebaseAuth.instance.fetchSignInMethodsForEmail(getEmail());
        if (list.isNotEmpty) {
          return 'Error';
        } else {
          await FirebaseAuth.instance.createUserWithEmailAndPassword(
              email: getEmail(), password: getPassword());
          DocumentReference ref = FirebaseFirestore.instance
              .collection('Users')
              .doc(FirebaseAuth.instance.currentUser!.uid);
          FirebaseFirestore.instance.runTransaction((transaction) async {
            DocumentSnapshot snapShot = await transaction.get(ref);
            if (!snapShot.exists) {
              ref.set({
                'name': getName(),
                'email': getEmail(),
              });
            }
          });
        }
      } else {
        return 'Error';
      }
    } on FirebaseAuthException catch (e) {
      return e.message;
    }
  }

  String get Email {
    return FirebaseAuth.instance.currentUser!.email.toString();
  }

  Future<String?> signOut() async {
    await FirebaseAuth.instance.signOut();
    return '';
  }

  login(String email, String password) async {
    _setEmail(email);
    _setPassword(password);
    if (getEmail() != 'Error' && getPassword() != 'Error') {
      try {
        await FirebaseAuth.instance.signInWithEmailAndPassword(
            email: getEmail(), password: getPassword());
        return 'Done';
      } on FirebaseAuthException catch (e) {
        return e.message;
      }
    }
  }

  _setName(String n) {
    _name = n;
  }

  getName() {
    if (_name == '') {
      return 'Error';
    } else {
      return _name;
    }
  }

  _setEmail(String e) {
    _email = e;
  }

  Future<String?> editProfile(
      {required String email, required String password}) async {
    try {
      _setEmail(email);
      _setPassword(password);
      if (getEmail() != 'Error' && getPassword() != 'Error') {
        final list =
            await FirebaseAuth.instance.fetchSignInMethodsForEmail(getEmail());
        if (list.isNotEmpty &&
            getEmail() != FirebaseAuth.instance.currentUser!.email) {
          return 'Error';
        } else {
          DocumentReference ref = FirebaseFirestore.instance
              .collection('Users')
              .doc(FirebaseAuth.instance.currentUser!.uid);
          FirebaseFirestore.instance.runTransaction((transaction) async {
            DocumentSnapshot snapShot = await transaction.get(ref);
            FirebaseAuth.instance.currentUser!.updatePassword(getPassword());
            FirebaseAuth.instance.currentUser!.updateEmail(getEmail());

            if (snapShot.exists) {
              transaction.update(ref, {
                'email': getEmail(),
              });
            }
          });
          return 'Done';
        }
      }
    } catch (e) {
      return 'Error';
    }
  }

  getEmail() {
    if (_email == '') {
      return 'Error';
    } else {
      return _email;
    }
  }

  _setPassword(String p) {
    _password = p;
  }

  getPassword() {
    if (_password == '') {
      return 'Error';
    } else {
      return _password;
    }
  }
}
