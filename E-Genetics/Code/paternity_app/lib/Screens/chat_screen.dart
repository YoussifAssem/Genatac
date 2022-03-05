// ignore_for_file: prefer_const_constructors, camel_case_types, must_be_immutable
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';


  final _firestore = FirebaseFirestore.instance;
  late User signedInUser; //the user
class ChatScreen extends StatefulWidget {
  static const String screenRoute = 'chat_screen';
    late String _title;
  Chat(String title) {
    _title = title;
  }

  ChatScreen({Key? key}) : super(key: key);

  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final messagetextcontroller = TextEditingController();
  final _auth = FirebaseAuth.instance;
  String? messageText; //the message

  // late String _title;
  // User _user = User();

  // _Chat(String title) {
  //   _title = title;
  // }

  @override
  void initState() {
    super.initState();
    getCurrentUser();
  }

  void getCurrentUser() {
    try {
      final user = _auth.currentUser;
      if (user != null) {
        signedInUser = user;
      }
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
  return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue[600],
        title : Center(
        child: Text('Chat', textAlign: TextAlign.center,),
        ),
      ),
      
        body : SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            messagestreambulder(),
            Container(
              decoration: const BoxDecoration(
                border: Border(
                  top: BorderSide(
                    color: Colors.black,
                    width: 2,
                  ),
                ),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Expanded(
                    child: TextField(
                      controller:messagetextcontroller,
                      onChanged: (value) {
                        messageText = value;
                      },
                      decoration: const InputDecoration(
                        contentPadding: EdgeInsets.symmetric(
                          vertical: 10,
                          horizontal: 20,
                        ),
                        hintText: 'Write your message here...',
                        border: InputBorder.none,
                      ),
                    ),
                  ),
                  TextButton(
                    onPressed: () {
                      messagetextcontroller.clear(); //to clear text feild
                      _firestore.collection('message').add({ //map key - value
                        'text': messageText,
                        //'sender': 'the sender',
                        'sender':signedInUser.email,
                        'time' : FieldValue.serverTimestamp(), //to arrange messages
                      });
                    },
                    child: Text(
                      'send',
                      style: TextStyle(
                        color: Colors.blue[800],
                        fontWeight: FontWeight.bold,
                        fontSize: 18,
                      ),
                    ),
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class messagestreambulder extends StatelessWidget {
  const messagestreambulder({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return  
    StreamBuilder<QuerySnapshot>(
              stream : _firestore.collection('message').orderBy('time').snapshots(), //oreder by to arrange massages
              builder: (context, snapshot){
                List<messageline> messagewidgets =[];

              if (!snapshot.hasData) //loading if there is no data found
              {
                return Center(
                  child :CircularProgressIndicator(
                    backgroundColor: Colors.blue,
                  ),
                );
              }

              final messages = snapshot.data!.docs.reversed; //reversed to show message is send
              for(var message in messages){
                final messagetext = message.get('text');
                final messagesender = message.get('sender');

                final currentuser = signedInUser.email;

                final messagewidget  = messageline(
                  sender:messagesender,
                  text:messagetext,
                  isme: currentuser == messagesender, // short if stament
                  );
                messagewidgets.add(messagewidget);
              }

                return Expanded(
                  child: ListView(
                    reverse: true,
                    padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  children : messagewidgets,
                  ),
                );
              },
              );
  }
}

class messageline extends StatelessWidget {
  messageline ({this.text, this.sender, required this.isme, Key? key }) : super(key: key);

  String? text;
  String? sender;
  final bool isme;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: Column(
        crossAxisAlignment: 
        isme ? CrossAxisAlignment.end : CrossAxisAlignment.start,
        children:[
          Text(
          '$sender',
          style: TextStyle(fontSize: 12, color: Colors.yellow[900]),
          ),
          Material(
            elevation: 5,
            borderRadius: isme? BorderRadius.only( //check the user to change the message color when typing
              topLeft: Radius.circular(30),
              bottomLeft: Radius.circular(30),
              bottomRight: Radius.circular(30),
            ) : BorderRadius.only(
              topRight: Radius.circular(30),
              bottomLeft: Radius.circular(30),
              bottomRight: Radius.circular(30),
            ),
          color: isme? Colors.blue[800] : Colors.white, //check the user to change the message color
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 10,horizontal: 10),
            child: Text('$text',
              style: TextStyle(fontSize: 15, color: isme? Colors.white : Colors.black45 )), //check the user to change the text color
          ),
        ),
        ]
      ),
    );
  }
}