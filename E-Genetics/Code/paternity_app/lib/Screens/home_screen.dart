// ignore_for_file: use_key_in_widget_constructors, camel_case_types

import 'package:flutter/material.dart';
import 'package:paternity_app/Models/user.dart';

class homeScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _homeScreen();
  }
}

class _homeScreen extends State<homeScreen> {
  User user = User();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 38, 54, 80),
      appBar: AppBar(
        backgroundColor: const Color.fromARGB(255, 38, 54, 80),
        title: const Text(
          'Welcome',
        ),
        actions: [
          Container(
            alignment: Alignment.centerRight,
            child: Text(
              user.Email,
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
          const SizedBox(
            height: 20,
          ),
          Container(
              padding: const EdgeInsets.all(10.0),
              child: const Text(
                ''' About Us: ''',
                textAlign: TextAlign.center,
                maxLines: 20,
                style: TextStyle(
                  fontSize: 20.0,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              )),
          Center(
            child: Column(
              children: [Image.asset('Images/paternity.jpg')],
            ),
          ),
          const SizedBox(
            height: 20,
          ),
          const Text(
            ''' ”Paternity Test” is an application dedicated to proving parentage and detecting child relevance. The most accurate aspect in determining the parents of a child is their DNA, to address one of the most significant phenomena that have spread around the world, that is homeless children. Orphaned children, and men who dispute the paternity of a child. We developed a method that analyzes the whole genome or alleles in a specific rs number. The proposed approach utilizes numerous algorithms to compare it to all of the individuals in the dataset. We applied methods to prove the parentage. Firstly, Mendelian's` law. Secondly, Short tandem repeat algorithm. Then, define the family of the orphan child. Additionally, the approach can determine whether or not the child is connected to his parents. Our experiment succeeded in proving or rejecting the relationship between the parent and child using the two approaches; either with RS or the whole genome.''',
            textAlign: TextAlign.center,
            maxLines: 20,
            style: TextStyle(
              fontSize: 16.0,
              fontWeight: FontWeight.w800,
              color: Colors.white,
            ),
          ),
        ],
      ),
    );
  }
}
