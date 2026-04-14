---
name: emmi-mobile-dev
description: >-
  Emmi mobile stack: Expo + Expo Router + NativeWind + Better Auth (Expo extension) + Zustand + TanStack Query.
  Native components everywhere except confirmation dialogs. Local builds, TestFlight distribution.
---

# Mobile dev

## Stack

| Layer | Technology | Role |
|-------|-----------|------|
| Framework | Expo (SDK latest) | App lifecycle, native modules, builds |
| Router | Expo Router | File-based navigation, deep links |
| Styling | NativeWind | Tailwind utility classes on native |
| Auth | Better Auth + Expo extension | Sessions, token storage, providers |
| Server state | TanStack Query (via tRPC or fetch) | Queries, mutations, cache |
| Client state | Zustand | Local UI state, non-server state |
| API | tRPC (monorepo) or REST (standalone) | Server communication |
| Builds | Local (Expo CLI) | iOS and Android |
| Distribution | TestFlight (iOS) | Beta testing |

---

## Project structure

```
app/
  (auth)/             # auth screens — sign in, sign up, forgot password
  (app)/              # protected screens
    (tabs)/           # bottom tab navigator
      index.tsx       # tab 1
      [feature]/      # tab with nested stack
        index.tsx
        [id].tsx
  _layout.tsx         # root layout, auth gate
  +not-found.tsx

components/
  ui/                 # shared primitive components
  [feature]/          # feature-specific components

lib/
  store/              # Zustand stores — one file per domain
  api/                # tRPC client or fetch wrapper
  auth.ts             # Better Auth Expo client

assets/
```

Screens and their components are grouped by feature, not by type. A feature's screen, its components, and its Zustand store live near each other.

---

## Navigation (Expo Router)

- **Expo Router only.** No React Navigation directly — Expo Router wraps it.
- **Default shell:** bottom tabs (`(tabs)/`) with nested stacks per tab. Each tab is its own navigation stack.
- **Auth gate in root layout.** `_layout.tsx` checks the session and redirects to `(auth)/` if unauthenticated. Screens inside `(app)/` never check auth themselves.
- **Deep links** are handled automatically by Expo Router's file structure. Document any meaningful deep link paths.
- **Typed routes** enabled — `expo-router/types` generates route types from the file system.

```ts
// app/_layout.tsx — root auth gate
const { session, isLoading } = useSession()

if (isLoading) return <SplashScreen />
if (!session) return <Redirect href="/(auth)/sign-in" />
```

---

## Styling (NativeWind)

- **NativeWind for all styling.** Same Tailwind mental model as web.
- **Use as many native components as possible.** `View`, `Text`, `TextInput`, `ScrollView`, `FlatList`, `Pressable`, `Image`, `Modal`, `ActivityIndicator` — prefer native over third-party wrappers.
- **Exception: confirmation dialogs.** Native `Alert.alert()` is visually inconsistent across platforms and ugly. Use a custom bottom sheet or modal for any confirmation or destructive action prompt.
- **Safe areas always.** Wrap screens in `SafeAreaView` or use `useSafeAreaInsets()`. Never hardcode padding for status bar or home indicator.
- **Keyboard handling.** Wrap forms in `KeyboardAvoidingView` with `behavior="padding"` on iOS. Test on both platforms.

---

## Auth (Better Auth + Expo extension)

Use the official Better Auth Expo extension. It handles:
- Session storage in SecureStore (not AsyncStorage — SecureStore is encrypted).
- Token refresh.
- Auth state across app restarts.

```ts
// lib/auth.ts
import { createAuthClient } from 'better-auth/expo'

export const authClient = createAuthClient({
  baseURL: process.env.EXPO_PUBLIC_API_URL,
})

export const { useSession, signIn, signOut } = authClient
```

- **Email/password default.** Other providers added per project on demand.
- **Biometrics on demand** — not a default. Add `expo-local-authentication` when the project requires it.
- **Never store tokens in AsyncStorage.** Always SecureStore via the Better Auth extension.

---

## Server state (TanStack Query)

Same pattern as web. All server communication goes through TanStack Query.

**Monorepo with tRPC:**
```ts
// Use the shared tRPC client from the monorepo packages/api
import { trpc } from '~/lib/api/trpc'
const { data } = trpc.posts.list.useQuery()
```

**Standalone app:**
```ts
// Wrap fetch in TanStack Query directly
const { data } = useQuery({
  queryKey: ['posts'],
  queryFn: () => fetch(`${API_URL}/posts`).then(r => r.json()),
})
```

- **Optimistic updates** on mutations — same rule as web: default to optimistic unless the user expects a wait.
- **Offline handling** — use TanStack Query's `staleTime` and `gcTime` to serve cached data when offline. Show a "you're offline" indicator rather than an error.

---

## Client state (Zustand)

Use Zustand for state that is not server-derived: UI state, local preferences, multi-step form state, feature flags.

One store per domain. Keep stores small and focused.

```ts
// lib/store/cart.ts
import { create } from 'zustand'

interface CartStore {
  items: CartItem[]
  add: (item: CartItem) => void
  remove: (id: string) => void
  clear: () => void
}

export const useCartStore = create<CartStore>((set) => ({
  items: [],
  add: (item) => set((s) => ({ items: [...s.items, item] })),
  remove: (id) => set((s) => ({ items: s.items.filter((i) => i.id !== id) })),
  clear: () => set({ items: [] }),
}))
```

Persist stores that need to survive app restarts with `zustand/middleware` persist + AsyncStorage.

---

## Builds and distribution

**Local builds only** — no EAS Build.

```bash
# iOS
npx expo run:ios --configuration Release

# Android
npx expo run:android --variant release
```

**Distribution:**
- iOS: TestFlight for beta testing. Archive in Xcode, upload to App Store Connect, distribute via TestFlight.
- Android: local APK/AAB for internal testing.

**No OTA updates by default.** Full builds for every release. Add EAS Update per project if OTA is required.

---

## Performance

- **FlashList** over `FlatList` for any list with more than ~20 items. Drop-in replacement with significantly better performance.
- **Memoize expensive components** with `React.memo` — only when profiling shows it helps. Don't pre-optimise.
- **Image sizing.** Always specify `width` and `height` on `Image`. Use `expo-image` over the built-in `Image` for caching and performance.
- **Avoid anonymous functions in render** on list items — extract to stable refs or components.

---

## Platform conventions

- **Android back button.** Handle with `useEffect` + `BackHandler` in screens that need custom back behaviour (e.g. confirm before leaving a form).
- **Haptics.** Use `expo-haptics` for confirm, delete, and toggle actions. Same rule as web — subtle and purposeful.
- **Share sheet.** Use `expo-sharing` or `Share.share()` wherever content is shareable.
- **Permissions.** Request permissions at the moment they are needed, not on app launch. Explain why before requesting.

---

## Feature build pattern

1. **Route file** — create the screen in `app/(app)/(tabs)/[feature]/`.
2. **Zustand store** — if the feature has local state, create `lib/store/[feature].ts`.
3. **API connection** — tRPC query/mutation or fetch wrapped in TanStack Query.
4. **Components** — in `components/[feature]/`, using native components + NativeWind.
5. **Auth guard** — handled by root layout, nothing to add per screen.
6. **Test on both platforms** before calling done. Safe areas, keyboard, back button.
