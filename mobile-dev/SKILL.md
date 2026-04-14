---
name: emmi-mobile-dev
description: >-
  Emmi preferred mobile stack: Expo with NativeWind (Tailwind-style RN). Use for app setup, navigation, native modules,
  OTA updates context, and sharing types/API with a Next.js backend when applicable.
---

# Mobile dev

## Stack

- **Expo** for app lifecycle, builds, and tooling.  
- **NativeWind** for utility-first styling aligned with web Tailwind mental model.  
- **API:** consume the same tRPC or REST layer as web when in a monorepo; share Zod schemas where possible.

## Conventions

- **Navigation:** predictable stacks and tabs; deep links documented.  
- **Auth:** secure token storage; refresh handling; biometric optional.  
- **Lists and perf:** flash lists / memoization where needed; image sizing.  
- **Platform quirks:** safe areas, keyboard, Android back.

## With Next.js backend

- Single source of truth for types; env-based API base URL; version API when breaking.

Use **ferdig-ferdig** with **Maestro** before major releases.
