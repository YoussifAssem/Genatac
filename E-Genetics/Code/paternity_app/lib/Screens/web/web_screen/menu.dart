// ignore_for_file: unused_field, use_key_in_widget_constructors

import 'package:flutter/material.dart';
import 'package:paternity_app/Screens/web/web_screen/editprofile.dart';
import 'package:paternity_app/Screens/web/web_screen/home_screen.dart';
import 'package:paternity_app/Screens/web/web_screen/login_screen.dart';
import 'package:paternity_app/Screens/web/web_screen/results_screen.dart';
import 'package:paternity_app/Screens/web/web_screen/view_chat.dart';

class Menu extends StatefulWidget {
  @override
  State<Menu> createState() => _Menu();
}

class _Menu extends State<Menu> {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      backgroundColor: Colors.blue[900],
      child: ListView(
        padding: EdgeInsets.zero,
        children: <Widget>[
          ListTile(
              leading: const Icon(Icons.home),
              title: const Text('Home'),
              iconColor: Colors.white,
              textColor: Colors.white,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => homeScreen()),
                );
              }),
          ListTile(
              leading: const Icon(Icons.chat),
              title: const Text('chat'),
              iconColor: Colors.white,
              textColor: Colors.white,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => viewChat()),
                );
              }),
          ListTile(
              leading: const Icon(Icons.grid_view),
              title: const Text('Results'),
              iconColor: Colors.white,
              textColor: Colors.white,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => Results()),
                );
              }),
          ListTile(
              leading: const Icon(Icons.edit),
              title: const Text('editprofile'),
              iconColor: Colors.white,
              textColor: Colors.white,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => EditProfilePage()),
                );
              }),
          ListTile(
              leading: const Icon(Icons.exit_to_app),
              title: const Text('Logout'),
              iconColor: Colors.white,
              textColor: Colors.white,
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => logIn()),
                );
              }),
        ],
      ),
    );
  }
}
