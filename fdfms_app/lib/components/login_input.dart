import 'package:flutter/material.dart';

class LoginInput extends StatelessWidget {
  final controller;
  final String labelText;
  final bool obscureText;

  const LoginInput({
    super.key,
    required this.controller,
    required this.labelText,
    required this.obscureText,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 25.0),
      child: TextField(
        controller: controller,
        obscureText: obscureText,
        decoration: InputDecoration(
          enabledBorder: const OutlineInputBorder(
            borderSide: BorderSide(
              color: Colors.black,
              width: 2,
            ),
          ),
          focusedBorder: const OutlineInputBorder(
            borderSide: BorderSide(
              color: Colors.white,
              width: 2,
            ),
          ),
          labelText: labelText,
          labelStyle: TextStyle(
            color: Colors.grey[500],
          ),
          fillColor: Colors.grey[100],
          filled: true,
        ),
      ),
    );
  }
}
