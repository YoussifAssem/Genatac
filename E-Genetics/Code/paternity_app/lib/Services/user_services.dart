// ignore_for_file: prefer_final_fields
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

// ignore: camel_case_types
class userServices {
  final FirebaseAuth _auth;

  userServices(this._auth);
  Future<String?> register(
      {required String name,
      required String email,
      required String password}) async {
    try {
      await _auth.createUserWithEmailAndPassword(
          email: email, password: password);
      DocumentReference ref = FirebaseFirestore.instance
          .collection('Users')
          .doc(_auth.currentUser!.uid);
      FirebaseFirestore.instance.runTransaction((transaction) async {
        DocumentSnapshot snapShot = await transaction.get(ref);
        if (!snapShot.exists) {
          ref.set({
            'name': name,
            'email': _auth.currentUser!.email,
          });
        }
      });
    } on FirebaseAuthException catch (e) {
      if (e.code == 'weak-password') {
        return e.message;
      } else if (e.code == 'email-already-in-use') {
        return e.message;
      } else {
        return e.message;
      }
    }
    return null;
  }

  String getEmail() {
    if (FirebaseAuth.instance.currentUser?.uid != null) {
      return FirebaseAuth.instance.currentUser!.email.toString();
    } else {
      return 'Null User';
    }
  }

  Future<String?> signOut() async {
    await _auth.signOut();
    return null;
  }

  Future<String?> logIn(String email, String password) async {
    try {
      await _auth.signInWithEmailAndPassword(email: email, password: password);
      return 'Done';
    } on FirebaseAuthException catch (e) {
      return e.message;
    }
  }

  Future<Object?> editProfile(
      {required String email, required String password}) async {
    try {
      DocumentReference ref = FirebaseFirestore.instance
          .collection('Users')
          .doc(_auth.currentUser!.uid);
      FirebaseFirestore.instance.runTransaction((transaction) async {
        DocumentSnapshot snapShot = await transaction.get(ref);
        _auth.currentUser!.updatePassword(password);
        _auth.currentUser!.updateEmail(email);

        if (snapShot.exists) {
          transaction.update(ref, {
            'email': email,
          });
        }
      });
    } catch (e) {
      return e;
    }
    return null;
  }
}
