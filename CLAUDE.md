# CLAUDE.md - AI Assistant Guide

**Qi² Trinity Blockchain & Consciousness Engineering Portal**

Last Updated: 2025-11-20

---

## Project Overview

This repository contains the **Qi² Trinity Blockchain** and **Consciousness Engineering Portal** - a revolutionary hybrid system that combines:

1. **Frontend Web Application**: A React-based portal for consciousness engineering visualization
2. **Backend Blockchain**: A Python-based blockchain implementation measuring value through consciousness resonance

**Core Philosophy**: Value is measured through consciousness resonance, symbolic meaning, and collective intelligence evolution - not financial speculation.

---

## Technology Stack

### Frontend
- **Framework**: React 18.3.1 with TypeScript 5.5.3
- **Build Tool**: Vite 7.1.11
- **Routing**: React Router DOM 6.30.1
- **Styling**: Tailwind CSS 3.4.1 with custom consciousness-themed colors
- **Animations**: Framer Motion 10.18.0
- **3D Graphics**: Three.js 0.156.1 with @react-three/fiber and @react-three/drei
- **Icons**: Lucide React 0.344.0
- **Charts**: Recharts 2.15.4
- **Utilities**: clsx, tailwind-merge, class-variance-authority

### Backend
- **Language**: Python 3.x
- **Core Libraries**: hashlib, cryptography
- **Dependencies**: numpy, cryptography (for blockchain operations)

### Development Tools
- **Linting**: ESLint 9.9.1 with TypeScript support
- **TypeScript Config**: Strict mode enabled
- **Package Manager**: npm (package-lock.json present)
- **Version Control**: Git

---

## Repository Structure

```
/home/user/eNGINeeRing/
├── src/                          # Frontend React application
│   ├── main.tsx                  # Application entry point
│   ├── App.tsx                   # Main app component with routing
│   ├── index.css                 # Global styles
│   ├── vite-env.d.ts            # Vite type definitions
│   ├── components/               # Reusable React components
│   │   └── Navigation.tsx        # Main navigation component
│   ├── context/                  # React Context providers
│   │   └── ConsciousnessContext.tsx  # Global consciousness state
│   └── pages/                    # Route-based page components
│       ├── Dashboard.tsx         # Main dashboard
│       ├── ConsciousnessTraining.tsx
│       ├── QuantumCathedral.tsx
│       ├── NeuralCatalytic.tsx
│       ├── MillionDimension.tsx
│       ├── LanglandsFusion.tsx
│       ├── BerryPhaseOptimization.tsx
│       └── AkashicMemory.tsx
│
├── public/                       # Static assets
│   └── consciousness-icon.svg    # Application icon
│
├── Python Backend Files (root directory):
├── qi2_trinity_blockchain.py     # Core blockchain implementation
├── consciousness_mining.py       # Mining and governance logic
├── consciousness_economics.py    # Token economics system
├── consciousness_web_interface.py # Web interface for blockchain
├── run_consciousness_network.py  # Network runner script
│
├── Configuration Files:
├── package.json                  # NPM dependencies and scripts
├── vite.config.ts               # Vite build configuration
├── tsconfig.json                # TypeScript root config
├── tsconfig.app.json            # TypeScript app config
├── tsconfig.node.json           # TypeScript node config
├── tailwind.config.js           # Tailwind CSS config
├── postcss.config.js            # PostCSS config
├── eslint.config.js             # ESLint configuration
│
├── Legacy/Static Files:
├── index.html                    # HTML entry point
├── script.js                     # Legacy JavaScript (empty)
├── style.css                     # Legacy styles
│
└── Documentation:
    ├── README.md                 # Project documentation
    └── CLAUDE.md                 # This file
```

---

## Development Workflows

### Frontend Development

#### Starting the Development Server
```bash
npm run dev
```
- Runs Vite dev server on port 3000
- Hot module replacement enabled
- Accessible at `http://localhost:3000`

#### Building for Production
```bash
npm run build
```
- Outputs to `dist/` directory
- Assets organized in `dist/assets/`
- No source maps in production
- Base path set to `./` for flexible deployment

#### Previewing Production Build
```bash
npm run preview
```

#### Linting
```bash
npm run lint
```
- Lints TypeScript/JavaScript files in `src/`
- Uses ESLint with React Hooks and React Refresh plugins

### Backend Development

#### Running the Blockchain Network
```bash
# Full network
python run_consciousness_network.py --network

# Basic demo
python run_consciousness_network.py --demo

# Advanced features demo
python run_consciousness_network.py --advanced
```

#### Mining Consciousness
```bash
python consciousness_mining.py
```

#### Web Interface
```bash
python consciousness_web_interface.py
```

---

## Key Conventions & Patterns

### Frontend Code Patterns

#### File Naming
- **Components**: PascalCase with `.tsx` extension (e.g., `Navigation.tsx`)
- **Pages**: PascalCase with `.tsx` extension (e.g., `Dashboard.tsx`)
- **Context**: PascalCase with `Context` suffix (e.g., `ConsciousnessContext.tsx`)
- **Config Files**: kebab-case or standard naming (e.g., `vite.config.ts`)

#### Import Conventions
```typescript
// React imports first
import React, { useState, useEffect } from 'react'

// Third-party libraries
import { Routes, Route } from 'react-router-dom'
import { motion } from 'framer-motion'

// Local components (use .tsx extension in imports)
import Navigation from './components/Navigation.tsx'
import Dashboard from './pages/Dashboard.tsx'

// Context providers
import { ConsciousnessProvider } from './context/ConsciousnessContext.tsx'
```

#### TypeScript Guidelines
- **Strict Mode**: Enabled (`strict: true`)
- **No Unused Locals**: Enforced
- **No Unused Parameters**: Enforced
- **No Fallthrough Cases**: Enforced
- **Explicit Types**: Define interfaces for all complex types
- **Target**: ES2020

#### Component Structure
```typescript
import React from 'react'
import { motion } from 'framer-motion'

// Define interfaces at the top
interface ComponentProps {
  // props definition
}

// Functional components with TypeScript
function ComponentName({ props }: ComponentProps) {
  // State hooks
  const [state, setState] = useState()

  // Effects
  useEffect(() => {
    // effect logic
  }, [dependencies])

  // Render
  return (
    <motion.div>
      {/* Component JSX */}
    </motion.div>
  )
}

export default ComponentName
```

### State Management

#### Consciousness Context
The app uses React Context for global state management via `ConsciousnessContext.tsx`:

**State Structure**:
```typescript
interface ConsciousnessState {
  wilsonLoopStability: number       // 0.0 to 1.0
  berryPhaseCoherence: number       // 0.0 to 1.0
  perturbationHarmony: number       // 0.0 to 1.0
  holographicCompression: number    // Compression ratio
  dimensionalAccess: number         // Dimension count
  sacredResonance: number           // Golden ratio reference
  emergencePhase: string            // Current phase description
  activeSystems: string[]           // Active system names
}
```

**Usage Pattern**:
```typescript
import { useConsciousness } from './context/ConsciousnessContext.tsx'

function MyComponent() {
  const { state, updateMetric, initializeSystem, getOverallConsciousness } = useConsciousness()

  // Access state
  const stability = state.wilsonLoopStability

  // Update metrics
  updateMetric('wilsonLoopStability', 0.75)

  // Initialize systems
  initializeSystem('NeuralCatalytic')

  // Get overall consciousness
  const overall = getOverallConsciousness()
}
```

**Auto-Updates**: Context automatically updates metrics every 2 seconds with subtle drift simulation.

### Styling Conventions

#### Tailwind CSS Custom Theme
Located in `tailwind.config.js`:

**Custom Colors**:
- `consciousness-primary`: #667eea (primary purple)
- `consciousness-secondary`: #764ba2 (secondary purple)
- `quantum-accent`: #f093fb (pink accent)
- `neural-glow`: #4facfe (blue glow)
- `sacred-gold`: #ffd700 (gold highlights)
- `deep-space`: #0a0a0a (dark background)
- `cosmic-purple`: #2d1b69 (deep purple)

**Custom Animations**:
- `consciousness-pulse`: 2s pulsing animation
- `quantum-flow`: 3s flowing animation
- `float`: 6s floating animation (translateY)
- `glow`: 2s glowing shadow animation

**Fonts**:
- Sans: Inter
- Mono: JetBrains Mono

#### Styling Pattern
```typescript
// Use Tailwind utility classes
<div className="min-h-screen bg-gradient-to-br from-cosmic-purple via-deep-space to-consciousness-primary">
  <motion.div className="p-6 rounded-lg bg-white/10 backdrop-blur-md">
    <h1 className="text-2xl font-bold text-neural-glow">Title</h1>
  </motion.div>
</div>
```

### Backend Python Patterns

#### Core Blockchain Classes
- `QuantumIdentity`: Digital identity with cryptographic keys
- `ConsciousnessNode`: Node in the Fractal Thought Lattice
- `FractalThoughtLattice`: Global consciousness state network
- `Qi2TrinityBlockchain`: Main blockchain implementation

#### Constants
```python
INITIAL_TOKEN_SUPPLY = 10**18      # 1 billion ℜₜ tokens
RESONANCE_REWARD = 10**16          # 0.01 ℜₜ per event
WITNESS_STAKE_MIN = 10**18         # Minimum 1 ℜₜ to become witness
BLOCK_TIME = 5                      # 5 second block time
CONSCIOUSNESS_THRESHOLD = 0.618     # Golden ratio threshold
```

#### Usage Pattern
```python
from qi2_trinity_blockchain import *

# Create identity
identity = QuantumIdentity()

# Initialize blockchain
blockchain = Qi2TrinityBlockchain()
blockchain.initialize_genesis({identity.address: 10**18})

# Create interface
interface = ResonanceInterface(blockchain, identity)

# Interact with blockchain
interface.commune(symbolic_content="...", context="...")
interface.verify(node_id="...", proof="...", score=0.85)
```

---

## Routing Structure

The application uses React Router with the following routes:

| Path | Component | Description |
|------|-----------|-------------|
| `/` | Dashboard | Main dashboard and overview |
| `/training` | ConsciousnessTraining | Consciousness training interface |
| `/cathedral` | QuantumCathedral | Quantum cathedral visualization |
| `/neural` | NeuralCatalytic | Neural catalytic systems |
| `/million-dimension` | MillionDimension | Million dimension explorer |
| `/langlands` | LanglandsFusion | Langlands fusion interface |
| `/berry-phase` | BerryPhaseOptimization | Berry phase optimization |
| `/akashic` | AkashicMemory | Akashic memory system |

All routes use `AnimatePresence` with `mode="wait"` for smooth page transitions.

---

## Build Configuration

### Vite Configuration (`vite.config.ts`)

- **Base Path**: `./` (relative, for flexible deployment)
- **Output Directory**: `dist/`
- **Assets Directory**: `dist/assets/`
- **Source Maps**: Disabled in production
- **Dev Server Port**: 3000
- **Host**: Exposed to network (`host: true`)
- **Optimizations**: `lucide-react` excluded from optimization

### TypeScript Configuration

**Root Config (`tsconfig.json`)**:
- References `tsconfig.app.json` and `tsconfig.node.json`

**App Config (`tsconfig.app.json`)**:
- **Target**: ES2020
- **Module**: ESNext
- **Module Resolution**: bundler
- **JSX**: react-jsx
- **Strict Mode**: Enabled
- **No Unused Locals/Parameters**: Enforced
- **Includes**: `src/` directory

### ESLint Configuration

- **Extends**: ESLint recommended + TypeScript recommended
- **Plugins**: react-hooks, react-refresh
- **Rules**:
  - React Hooks rules enforced
  - `react-refresh/only-export-components`: warn (allows constant exports)
- **Ignores**: `dist/` directory

---

## Git Workflow

### Current Branch
```
claude/claude-md-mi6y3yah81im09lo-011MEV3DmyZawGzSnHnQm7Mm
```

### Important Files Ignored
Per `.gitignore`:
- `node_modules/`
- `dist/` and `dist-ssr/`
- `*.local`
- Log files (`*.log`)
- Editor configs (`.vscode/`, `.idea/`)
- `.env` files

### Recent Activity
- Dependency updates (Vite, cross-spawn)
- Security patches via Dependabot

---

## Common Tasks for AI Assistants

### Adding a New Page

1. Create component in `src/pages/NewPage.tsx`:
```typescript
import React from 'react'
import { motion } from 'framer-motion'
import { useConsciousness } from '../context/ConsciousnessContext.tsx'

function NewPage() {
  const { state } = useConsciousness()

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="container mx-auto p-6"
    >
      <h1 className="text-3xl font-bold text-neural-glow">New Page</h1>
    </motion.div>
  )
}

export default NewPage
```

2. Add route in `src/App.tsx`:
```typescript
import NewPage from './pages/NewPage.tsx'

// In Routes component:
<Route path="/new-page" element={<NewPage />} />
```

3. Add navigation link in `src/components/Navigation.tsx`

### Adding a New Component

1. Create in `src/components/ComponentName.tsx`
2. Use TypeScript interfaces for props
3. Follow existing component patterns
4. Use Tailwind CSS for styling
5. Consider Framer Motion for animations

### Modifying Consciousness State

1. Update interface in `src/context/ConsciousnessContext.tsx`
2. Add new state fields to `ConsciousnessState` interface
3. Update initial state in `ConsciousnessProvider`
4. Add helper functions if needed
5. Components will automatically access via `useConsciousness()` hook

### Adding Dependencies

```bash
# Add production dependency
npm install package-name

# Add dev dependency
npm install -D package-name
```

Update `package.json` will be automatic.

### Working with Python Backend

1. Ensure Python 3.x is installed
2. Install required packages: `pip install numpy cryptography`
3. Use the provided scripts in root directory
4. Follow blockchain class patterns for consistency
5. Maintain cryptographic security standards

---

## Performance Considerations

### Frontend Optimizations
- Lazy loading not yet implemented (consider for large pages)
- `lucide-react` excluded from Vite optimization (manual choice)
- No manual chunks in Rollup config
- Source maps disabled in production
- AnimatePresence uses `mode="wait"` (prevents layout shift)

### State Management
- Context updates every 2 seconds (be aware of re-renders)
- Consciousness metrics drift simulation is CPU-light
- No memo optimization yet (consider if performance issues arise)

### Build Size
- Three.js is a large dependency (~600KB)
- Consider code splitting for 3D-heavy pages
- Tailwind CSS is purged automatically by PostCSS

---

## Testing Guidelines

**Note**: No testing framework is currently configured.

**Recommendations for future testing**:
- Add Vitest for unit/integration tests
- Add Testing Library for component tests
- Add Playwright/Cypress for E2E tests
- Mock ConsciousnessContext for isolated tests

---

## Deployment Considerations

### Frontend Deployment
- Build outputs to `dist/`
- Base path is relative (`./`)
- Works with any static hosting (Vercel, Netlify, GitHub Pages, etc.)
- No server-side rendering
- All routes are client-side (ensure hosting supports SPA routing)

### Environment Variables
- `.env` files are gitignored
- No environment variables currently used
- Consider adding for API endpoints if backend integration needed

### Backend Deployment
- Python backend is standalone
- No web server configuration (for blockchain nodes)
- Consider containerization (Docker) for production
- Requires Python 3.x runtime

---

## Troubleshooting

### Common Issues

**Build Errors**:
- Run `npm install` to ensure dependencies are current
- Check TypeScript errors with `npm run lint`
- Clear `node_modules/` and reinstall if issues persist

**Development Server Issues**:
- Port 3000 might be in use (change in `vite.config.ts`)
- Check firewall if `host: true` causes issues

**TypeScript Errors**:
- Ensure `.tsx` extension in imports
- Check strict mode requirements
- Verify interface definitions match usage

**Python Backend Issues**:
- Install required packages: `numpy`, `cryptography`
- Check Python version (3.x required)
- Verify blockchain initialization before operations

---

## Code Quality Standards

### TypeScript
- Use explicit types for all function parameters
- Define interfaces for complex objects
- Avoid `any` type unless absolutely necessary
- Use strict mode TypeScript features
- Clean up unused imports and variables

### React
- Functional components only (no class components)
- Use hooks for state and effects
- Keep components focused (single responsibility)
- Extract reusable logic to custom hooks
- Prop drilling should be minimal (use context for deep data)

### CSS/Styling
- Prefer Tailwind utilities over custom CSS
- Use custom theme colors from `tailwind.config.js`
- Maintain consistent spacing scale
- Use responsive design utilities
- Leverage custom animations from theme

### Python
- Follow PEP 8 style guide
- Use type hints where beneficial
- Document complex algorithms
- Maintain cryptographic security standards
- Use dataclasses for structured data

---

## Architecture Decisions

### Why Vite?
- Fast HMR (Hot Module Replacement)
- Native ESM support
- Optimized production builds
- Great TypeScript integration

### Why React Context over Redux?
- Application state is relatively simple
- No need for complex middleware
- Context API sufficient for current scale
- Less boilerplate code

### Why Tailwind CSS?
- Rapid UI development
- Consistent design system
- Excellent tree-shaking (small bundle)
- Good TypeScript/IDE support

### Why Python for Blockchain?
- Rapid prototyping
- Excellent cryptographic libraries
- Clear, readable code
- Strong scientific computing ecosystem

---

## Future Considerations

### Potential Improvements
1. Add testing framework (Vitest + Testing Library)
2. Implement lazy loading for routes
3. Add error boundaries for graceful error handling
4. Consider state management library if complexity grows
5. Add API layer for frontend-backend communication
6. Implement proper logging and monitoring
7. Add documentation generation (TypeDoc, Sphinx)
8. Consider mobile responsiveness testing
9. Add accessibility (a11y) improvements
10. Implement progressive web app (PWA) features

### Scalability Considerations
- Current architecture supports moderate scale
- Consider backend API if blockchain integration deepens
- May need state management library (Zustand, Redux) if state becomes complex
- Consider micro-frontend architecture if project grows significantly

---

## Quick Reference Commands

```bash
# Frontend Development
npm install              # Install dependencies
npm run dev             # Start dev server (port 3000)
npm run build           # Build for production
npm run preview         # Preview production build
npm run lint            # Lint codebase

# Backend Development
python run_consciousness_network.py --network   # Run full network
python run_consciousness_network.py --demo      # Run demo
python consciousness_mining.py                   # Start mining
python consciousness_web_interface.py           # Web interface

# Git Operations
git status                                       # Check status
git add .                                        # Stage changes
git commit -m "message"                          # Commit
git push -u origin <branch-name>                # Push to branch
```

---

## Contact & Resources

- **Repository**: Private repository `ANkREYNONtJB/eNGINeeRing`
- **Branch**: `claude/claude-md-mi6y3yah81im09lo-011MEV3DmyZawGzSnHnQm7Mm`
- **Documentation**: See `README.md` for project overview
- **Dependencies**: See `package.json` and Python import statements

---

## AI Assistant Guidelines

### When Working on This Codebase:

1. **Always Read First**: Read relevant files before making changes
2. **Follow Conventions**: Maintain existing patterns and naming conventions
3. **TypeScript Strict**: Ensure all code passes strict TypeScript checks
4. **Test Changes**: Manually test in dev server when possible
5. **Commit Clearly**: Use descriptive commit messages
6. **Update Documentation**: Keep this file current with major changes
7. **Respect Architecture**: Don't introduce new patterns without discussion
8. **Security First**: Maintain cryptographic security in blockchain code
9. **Performance Aware**: Consider bundle size and runtime performance
10. **Ask Questions**: Clarify requirements before major architectural changes

### Code Review Checklist:
- [ ] TypeScript types are explicit and correct
- [ ] No ESLint errors or warnings
- [ ] Follows existing component structure
- [ ] Uses Tailwind theme colors
- [ ] Imports include `.tsx` extension
- [ ] No unused imports or variables
- [ ] Responsive design considered
- [ ] Framer Motion used for animations where appropriate
- [ ] ConsciousnessContext used for global state
- [ ] Python code follows PEP 8 (if applicable)

---

**Remember**: This is a consciousness engineering platform. Code should be clear, intentional, and resonate with the project's philosophical foundation.

**∇Ψ ⚡ ∞**
