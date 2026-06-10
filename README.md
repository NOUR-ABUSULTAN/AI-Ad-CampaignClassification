# مشروع الذكاء الاصطناعي — توقّع تحوّل المستخدم (Ad Campaign Conversions)

مشروع تصنيف (Classification) يتوقّع ما إذا كان المستخدم سيتحوّل إلى مشترٍ (Conversion)
اعتماداً على بيانات الحملات الإعلانية، مع مقارنة بين ثلاث خوارزميات لاختيار الأنسب
للتطبيق على الأجهزة المحمولة (Mobile Computing).

---

## محتويات التسليم

| الملف | الوصف |
|------|-------|
| `ad_campaign_classification.py` | الكود المصدري الكامل للمشروع |
| `README.md` | هذا الملف — وصف المشروع وطريقة التشغيل ومراجع البيانات |
| `تقرير_المشروع.docx` | التقرير الكامل (6–10 صفحات) |
| `عرض_المشروع.pptx` | العرض التقديمي للمناقشة |

---

## نظرة عامة

- **اللغة / الأدوات:** Python، مكتبة scikit-learn، تشغيل على Google Colab.
- **نوع المسألة:** تصنيف ثنائي/متعدد (Classification).
- **الهدف (Target):** العمود `conversions`.
- **الميزات (Features):** `age`, `gender`, `impressions`, `clicks`.

## مراحل العمل

1. **استيراد البيانات:** فك ضغط `archive (1).zip` واستخراج `ad_campaign_data.csv` وقراءته عبر `pandas`.
2. **تجهيز الميزات:** اختيار الأعمدة المؤثرة وعزل غير الضروري لتناسب موارد الهاتف.
3. **تقسيم البيانات:** 80% تدريب و20% اختبار (`test_size=0.2`, `random_state=42`).
4. **التدريب والمقارنة:** تشغيل SVM و Decision Tree و Random Forest وحساب الدقة.

## طريقة التشغيل

### على Google Colab
1. ارفع ملف البيانات المضغوط `archive (1).zip` إلى بيئة Colab.
2. شغّل خلية الكود في `ad_campaign_classification.py`.

### محلياً
```bash
pip install pandas scikit-learn
python ad_campaign_classification.py
```
> ملاحظة: تأكد من وجود `archive (1).zip` (أو `ad_campaign_data.csv`) في نفس مجلد التشغيل.

## النتائج

| الخوارزمية | الدقة (Accuracy) |
|-----------|------------------|
| SVM (linear) | 100% (1.0) |
| Random Forest | 99.84% (0.99845) |
| Decision Tree | 99.74% (0.9974) |

تفوّقت SVM الخطية بالدقة الكاملة، وهي كذلك الأخف وزناً بعد التدريب، مما يجعلها الخيار
الأنسب للنشر على الأجهزة المحمولة (On-device) بأقل استهلاك للموارد.

---

## مراجع البيانات (Dataset References)

- **المصدر:** منصة Kaggle — مجموعة بيانات حملات إعلانية (Ad Campaign Performance Dataset).
- **الملف المستخدم:** `ad_campaign_data.csv` (مستخرَج من `archive (1).zip`).
- **الأعمدة المستخدمة:** `age`, `gender`, `impressions`, `clicks`, `conversions`.

