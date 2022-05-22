// ignore_for_file: unused_field, use_key_in_widget_constructors

import 'package:flutter/material.dart';
import 'package:paternity_app/Screens/editprofile.dart';
import 'package:paternity_app/Screens/home_screen.dart';
import 'package:paternity_app/Screens/login_screen.dart';
import 'package:paternity_app/Screens/results_screen.dart';
import 'package:paternity_app/Screens/view_chat.dart';

class Menu extends StatefulWidget {
  @override
  State<Menu> createState() => _Menu();
}

class _Menu extends State<Menu> {
  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  final List<Widget> _widgetOptions = <Widget>[
    homeScreen(),
    viewChat(),
    Results(),
    EditProfilePage(),
    logIn(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
      if (_selectedIndex == 4) {
        Navigator.pushReplacement(
            context, MaterialPageRoute(builder: (context) => logIn()));
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent,
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
            backgroundColor: Color.fromARGB(255, 38, 54, 80),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.chat),
            label: 'Chat',
            backgroundColor: Color.fromARGB(255, 38, 54, 80),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.grid_view),
            label: 'Results',
            backgroundColor: Color.fromARGB(255, 38, 54, 80),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.edit),
            label: 'Edit Profile',
            backgroundColor: Color.fromARGB(255, 38, 54, 80),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.logout),
            label: 'Log Out',
            backgroundColor: Color.fromARGB(255, 38, 54, 80),
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.white,
        onTap: _onItemTapped,
      ),
    );
  }
}
