import 'package:flutter/material.dart';

import 'package:fdfms_app/components/login_input.dart';

class LoginPage extends StatelessWidget {
  LoginPage({super.key});

  // Inputs controllers
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[300],
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Align(
                alignment: Alignment.center,
                child: Text(
                  'Food Delivery Fleet Management System',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 30,
                  ),
                )),
            const SizedBox(height: 20),

            // Username
            LoginInput(
              controller: usernameController,
              labelText: 'Username',
              obscureText: false,
            ),
            // Username

            const SizedBox(height: 20),

            // Forgot password
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 25.0),
              child: Align(
                alignment: Alignment.centerRight,
                child: TextButton(
                  onPressed: () {},
                  child: Text(
                    'Forgot password?',
                    style: TextStyle(color: Colors.grey[500], fontSize: 12),
                  ),
                ),
              ),
            ),

            // Password
            LoginInput(
              controller: passwordController,
              labelText: 'Password',
              obscureText: true,
            ),
            // Password

            ElevatedButton(
              onPressed: () {},
              child: const Text('Login'),
            ),
          ],
        ),
      ),
    );
  }
}
