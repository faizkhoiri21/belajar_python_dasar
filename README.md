
# 🧾 Laporan Evaluasi Model NER Bahasa Indonesia

## 1. Deskripsi Umum
Model Named-Entity Recognition (NER) ini dilatih untuk mengenali berbagai jenis entitas dalam teks berita berbahasa Indonesia, seperti **Person (PER)**, **Organization (ORG)**, **Location (LOC)**, **Geopolitical Entity (GPE)**, **Law (LAW)**, **Money (MONEY)**, dan **Date (DATE)**.  
Evaluasi dilakukan pada *test set* menggunakan metrik **Precision**, **Recall**, dan **F1-Score**, serta divisualisasikan melalui **Confusion Matrix**.

---

## 2. Hasil Umum

| Metric | Nilai |
|:-------|:------|
| **Micro F1-Score** | 0.7429 |
| **Macro F1-Score** | 0.6603 |
| **Weighted F1-Score** | 0.7447 |

**Interpretasi:**  
Model mencapai **F1-Score rata-rata 74%**, menunjukkan performa cukup baik dalam mendeteksi entitas umum.  
Perbedaan antara *macro* dan *micro F1* menandakan performa antar-label **belum merata**.

---

## 3. Performa per Label

| Label | Precision | Recall | F1-Score | Analisis |
|:------|:-----------|:--------|:----------|:----------|
| **B-DATE** | 0.65 | 0.69 | 0.67 | Cukup baik mengenali tanggal/waktu, tapi masih keliru pada konteks tahun/bulan. |
| **B-EVENT** | 0.48 | 0.60 | 0.51 | Sering tertukar dengan ORG atau LOC (mis. “Festival Jakarta Fair”). |
| **B-FAC** | 0.55 | 0.60 | 0.57 | Kesulitan membedakan fasilitas dari lokasi umum. |
| **B-GPE** | 0.76 | 0.94 | **0.85** | Salah satu label terkuat – wilayah/negara dikenali sangat baik. |
| **B-LAW** | 0.46 | 0.57 | 0.51 | Lemah karena data latih sedikit dan format bervariasi. |
| **B-LOC** | 0.42 | 0.42 | 0.42 | Sering tertukar dengan GPE (lokasi vs wilayah administratif). |
| **B-MONEY** | 0.87 | 0.92 | **0.90** | Sangat tinggi – pola angka & mata uang mudah dikenali. |
| **B-ORG** | 0.66 | 0.77 | 0.71 | Cukup stabil; kadang salah deteksi terhadap event. |
| **B-PER** | 0.80 | 0.86 | **0.83** | Label paling akurat – nama orang dikenali konsisten. |

---

## 4. Analisis Confusion Matrix
<p align="center">
  <img src="https://ibb.co.com/svzWzDB1" alt="Confusion Matrix" width="500">
</p>

- **Diagonal biru tua** → prediksi benar (model yakin).  
- **Warna terang di luar diagonal** → kesalahan umum.  

**Pola kesalahan utama:**
- `B-LOC → B-GPE` → lokasi sering dikira wilayah administratif.  
- `B-EVENT ↔ B-ORG` → acara kadang dianggap organisasi.  
- `I-` label (token lanjutan) lebih lemah dibanding `B-` label.

**Kesimpulan visual:**
- Model unggul pada **PER**, **ORG**, **MONEY**, **GPE**.  
- Perlu peningkatan pada **EVENT**, **LOC**, **LAW**, dan entitas multi-kata.

---

## 5. Kekuatan Model
✅ Deteksi entitas besar akurat (PER, ORG, MONEY, GPE).  
✅ Minim false positive – token non-entitas dikenali baik.  
✅ Pelatihan stabil tanpa indikasi overfitting berat.

---

## 6. Kelemahan Model
⚠️ Lemah di label minor (EVENT, LAW, LOC).  
⚠️ Kesalahan umum pada token lanjutan (I- prefix).  
⚠️ Bias terhadap label dominan karena distribusi tidak seimbang.

---

## 7. Rekomendasi Perbaikan
1. **Data augmentasi** untuk label minor.  
2. **Perpanjang konteks** (`max_length=512`, `stride=192`).  
3. **Label smoothing** (0.05–0.1) untuk reduksi noise.  
4. **Tambahkan CRF layer** di atas classifier.  
5. **Gunakan model lebih besar**, mis. `xlm-roberta-large` atau `indobert-large-p1`.  
6. **Fine-tuning sweep** kecil pada *learning rate* (`1e-5` s.d. `3e-5`).

---

## 8. Kesimpulan Akhir
Model NER mencapai **F1-Score keseluruhan 74%**, menandakan performa solid dalam mengenali entitas umum.  
Namun, performa antar-label belum seimbang — peningkatan disarankan untuk label minor dan token lanjutan agar performa model merata di semua label.

---
