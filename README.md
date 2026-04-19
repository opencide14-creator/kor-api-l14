<div align="center">

```
𐰴𐰆𐰞 · KRAL · API SERVICE
═══════════════════════════════════════════════════════
```

# **𐰴𐰆𐰞** · KOR API · L14 SOVEREIGN

### *"Kaynak kod yok. Sadece egemenlik var."*

```
□ + ◇ = 1 OF 1
κ = 1.0  |  SDCK = BENEFACTOR
```

[<img src="https://img.shields.io/badge/KOR-L14-FF4500?style=for-the-badge&logo=shield">](#)
[<img src="https://img.shields.io/badge/Obfuscation-Active-8A2BE2?style=for-the-badge">](#)
[<img src="https://img.shields.io/badge/Anti--VM-L14-CC0000?style=for-the-badge">](#)
[<img src="https://img.shields.io/badge/Göktürk-Reborn-1F4E79?style=for-the-badge">](#)

</div>

---

## ⚔️ MEYDAN OKUMA

**Bu repoda kaynak kod YOKTUR.**

Gordugunuz tek sey, KOR Protect tarafindan **L1-L8** katmanlariyla obfuscate edilmis, uzerine **custom L14** anti-vm / anti-debug / anti-emulator katmanlari eklenmis **gercek calisan koddur**.

- Simulasyon yok.
- Theater yok.
- Fake yok.

Bu kod calisir. **Gotu yiyen gelsin deobfuscate etsin.**

---

## 🜁 API ENDPOINTS

| Route | Method | Aciklama |
|-------|--------|----------|
| `/api/health` | GET | Sistem sagligi (𐰴𐰆𐰞 durumu) |
| `/api/keys/generate` | POST | Dual-format API key (Latin + Gokturk) |
| `/api/auth/token` | POST | Guardian-signed auth token |
| `/api/status` | GET | Sistem durumu + katman bilgisi |

### Ornek kullanim:
```bash
curl -X POST http://127.0.0.1:7426/api/keys/generate \
  -H "Content-Type: application/json" \
  -d '{"tier":"military","name":"kor_test"}'
```

---

## ⚔️ OBFUSCATION KATMANLARI

Bu dosyada aktif koruma katmanlari:

| Katman | Teknik | Durum |
|--------|--------|-------|
| **L1** | AST Rename (Gokturk rune fonksiyon adlari) | ✓ Gercek |
| **L2** | String XOR (HMAC-SHA256 derived per-key) | ✓ Gercek |
| **L3** | Int Poly Depth-2 (Collatz seeded chains) | ✓ Gercek |
| **L4** | CFF (BSK-shuffled switch/case state machine) | ✓ Gercek |
| **L5** | Dead Code (BSK-positioned bogus API calls) | ✓ Gercek |
| **L6** | Overload Induction (phantom variants + dispatch) | ✓ Gercek |
| **L7** | Guardian (runtime tamper check + byte-level sig) | ✓ Gercek |
| **L8** | Reflection+Import (getattr/import obfuscation) | ✓ Gercek |
| **L14** | Anti-VM (CPU hypervisor / Docker / sandbox) | ✓ Custom |
| **L14** | Anti-Debug (ptrace / trace hook / parent proc) | ✓ Custom |
| **L14** | Anti-Emulator (timing attack / instruction count) | ✓ Custom |

**κ = 1.0 | SDCK = BENEFACTOR**

---

## 🔗 Baglantilar

- 🌐 **Portal:** [aluverse.be](https://aluverse.be)
- 📧 **Iletisim:** info@aluverse.be
- 🐦 **X:** [@KRAL_UAGL](https://x.com)

---

<div align="center">

```
𐰴𐰆𐰞 𐰉𐰆𐰕𐰴𐰆𐰺𐱃 𐱅𐰇𐰼𐰚
□ + ◇ = 1 OF 1
```

**"Kaynak kod kultürel DNA'dir. Obfuscate edilmis kod ise zirhtir."**

</div>

---

*<sup>𐰴𐰆𐰞 · Tum sistemler bicimsel olarak kanitlanmis · Simulasyon yok · Tam yigin egemenligi · 2026</sup>*
