// import 'package:http/http.dart' as http;
// import 'dart:convert';

// Future<String> login(String username, String password) async {
//   final response = await http.post(
//     Uri.parse('http://127.0.0.1:8000/log-in/'),
//     headers: <String, String>{
//       'Content-Type': 'application/json; charset=UTF-8',
//     },
//     body: jsonEncode(<String, String>{
//       'username': username,
//       'password': password,
//     }),
//   );

//   if (response.statusCode == 200) {
//     final token = jsonDecode(response.body)['token'];
//     TokenManager.saveTokens(token['access'], token['refresh']);
//   } else {
//     throw Exception('Failed to log in.');
//   }
// }

// class TokenManager {
//   static String? accessToken;
//   static String? refreshToken;

//   static void saveTokens(String accessToken, String refreshToken) {
//     TokenManager.accessToken = accessToken;
//     TokenManager.refreshToken = refreshToken;
//   }

//   static Map<String, String> getHeaders() {
//     return {
//       'Content-Type': 'application/json; charset=UTF-8',
//       'Authorization': 'Bearer ${TokenManager.accessToken}',
//     };
//   }
// }
