html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ai Protection 🛡️</title>
<style>
* {box-sizing:border-box}
body {
    margin:0;
    font-family:Arial,sans-serif;
    background:#080d18;
    color:white;
    text-align:center;
}
header {
    padding:65px 20px 35px;
    background:linear-gradient(135deg,#102b50,#080d18);
}
.logo {
    font-size:65px;
}
h1 {
    font-size:35px;
    color:#50b5ff;
}
.subtitle {
    color:#b6c5d9;
    font-size:17px;
}
.container {
    max-width:750px;
    margin:30px auto;
    padding:15px;
}
.card {
    background:#111c2e;
    border:1px solid #263c59;
    border-radius:16px;
    padding:20px;
    margin:15px 0;
    text-align:right;
}
.card h2 {
    color:#50b5ff;
    font-size:21px;
}
.card p {
    color:#d0d9e8;
    line-height:1.8;
}
.rules {
    background:#172338;
    padding:22px;
    border-radius:16px;
    line-height:2.2;
    text-align:right;
}
button {
    background:#1689e8;
    border:0;
    padding:14px 28px;
    border-radius:10px;
    color:white;
    font-size:17px;
    cursor:pointer;
}
footer {
    padding:30px;
    color:#71839e;
}
</style>
</head>
<body>

<header>
<div class="logo">🛡️</div>
<h1>Ai Protection</h1>
<p class="subtitle">حارس ذكي لقروبك — شغّال الحين.</p>
</header>

<div class="container">

<div class="card">
<h2>🤖 الذكاء الاصطناعي</h2>
<p>يرد على أسئلتك بذكاء. منشن البوت في القروب واسأله أي شيء.</p>
</div>

<div class="card">
<h2>👑 صلاحيات الإدارة</h2>
<p>يعرف المالك والمشرفين. أوامر الطرد والحظر والكتم للمالك والمشرفين فقط.</p>
</div>

<div class="card">
<h2>🔗 منع الروابط</h2>
<p>يحذف الروابط التي يرسلها الأعضاء ويحذر المخالفين.</p>
</div>

<div class="card">
<h2>🖼️ فحص الصور</h2>
<p>يفحص الصور ويحذف المحتوى المخالف تلقائياً.</p>
</div>

<div class="card">
<h2>🎧 الرسائل الصوتية</h2>
<p>يستمع للرسائل الصوتية في الخاص، أو عند الرد على الصوتية ومنشن البوت في القروب.</p>
</div>

<div class="card">
<h2>⚠️ نظام التحذيرات</h2>
<p>3 تحذيرات = طرد العضو، مع رسالة ترحيب لكل عضو جديد.</p>
</div>

<div class="card">
<h2>📜 قوانين البوت</h2>
<div class="rules">
1. يمنع إرسال الروابط غير المسموح بها.<br>
2. يمنع نشر الصور أو المحتوى غير اللائق.<br>
3. احترام جميع أعضاء المجموعة.<br>
4. يمنع إزعاج البوت أو استغلال أوامره.<br>
5. أوامر الإدارة للمالك والمشرفين فقط.<br>
6. الالتزام بتعليمات مشرفي المجموعة.<br>
7. عند الحصول على 3 تحذيرات يتم الطرد.
</div>
</div>

<div class="card">
<h2>💬 أمثلة الاستخدام</h2>
<p>
• رد على رسالة شخص واكتب: @البوت طلع هذا<br><br>
• @البوت احظر @username<br><br>
• @البوت اكتم<br><br>
• @البوت فك الكتم<br><br>
• @البوت حذره<br><br>
• @البوت وش عاصمة اليابان؟
</p>
</div>

</div>

<footer>
🛡️ Ai Protection — حماية مجموعتك بذكاء
</footer>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("تم إنشاء موقع Ai Protection بنجاح!")
