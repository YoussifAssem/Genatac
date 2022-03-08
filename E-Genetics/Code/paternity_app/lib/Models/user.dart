// ignore_for_file: non_constant_identifier_names

import 'package:firebase_auth/firebase_auth.dart';
import 'package:paternity_app/Services/user_services.dart';

class User {
  // ignore: prefer_final_fields, unused_field
  late String _name;
  late String _email;
  late String _password;
  userServices uS = userServices(FirebaseAuth.instance);

  signUp({
    required String name,
    required String email,
    required String password,
  }) async {
    _setName(name);
    _setEmail(email);
    _setPassword(password);
    await uS.register(
        name: getName(), email: getEmail(), password: getPassword());
    if (_checkUser() == '') {
      return '';
    } else {
      return 'Error';
    }
  }

  String get Email {
    return uS.getEmail();
  }

  Future<String?> signOut() async {
    await uS.signOut();
    return null;
  }

  login(String email, String password) async {
    userServices u = userServices(FirebaseAuth.instance);
    _setEmail(email);
    _setPassword(password);
    if (await u.logIn(getEmail(), getPassword()) == 'Done') {
      return '';
    } else {
      return 'Error';
    }
  }

  _checkUser() {
    if (_name == '' || _email == '' || _password == '') {
      return 'Error';
    } else {
      return '';
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

  Future<Map<String, dynamic>?> editProfile(
      {required String e, required String password}) async {
    await uS.editProfile(email: e, password: password);
    return null;
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
