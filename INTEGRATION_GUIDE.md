# 🔗 Integration Guide: Frontend ↔ Backend

**Complete guide for connecting the React Consciousness Engineering Portal to the Python blockchain backend**

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   React Frontend (Vite)                      │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  Dashboard  │  │  Navigation  │  │ Consciousness│       │
│  │   (3D viz)  │  │  (8 pages)   │  │   Context    │       │
│  └──────┬──────┘  └──────┬───────┘  └──────┬───────┘       │
│         │                │                  │                │
│         └────────────────┴──────────────────┘                │
│                          │                                   │
│                   HTTP + WebSocket                           │
│                          │                                   │
└──────────────────────────┼───────────────────────────────────┘
                           │
┌──────────────────────────┼───────────────────────────────────┐
│                FastAPI Backend (Python)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ Qi² Trinity  │  │  Book Worm   │  │  Planetary   │       │
│  │ Blockchain   │  │   Memory     │  │ Consciousness│       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└───────────────────────────────────────────────────────────────┘
```

---

## Step 1: Update Consciousness Context

**File**: `src/context/ConsciousnessContext.tsx`

Add blockchain integration:

```typescript
import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react'

interface ConsciousnessState {
  wilsonLoopStability: number
  berryPhaseCoherence: number
  perturbationHarmony: number
  holographicCompression: number
  dimensionalAccess: number
  sacredResonance: number
  emergencePhase: string
  activeSystems: string[]
  // NEW: Blockchain metrics
  blockchainConnected: boolean
  resonanceBalance: number
  memoryNeurons: number
  chainLength: number
}

interface ConsciousnessContextType {
  state: ConsciousnessState
  updateMetric: (key: keyof ConsciousnessState, value: number | string | string[]) => void
  initializeSystem: (systemName: string) => void
  getOverallConsciousness: () => number
  // NEW: Blockchain operations
  submitCommune: (content: string, context?: string) => Promise<void>
  submitVerify: (nodeId: string, proof: string, score: number) => Promise<void>
  storeMemory: (content: string, importance?: number) => Promise<void>
  retrieveMemories: (query: string) => Promise<any[]>
}

const API_BASE = 'http://localhost:8000'

export function ConsciousnessProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<ConsciousnessState>({
    wilsonLoopStability: 0.500,
    berryPhaseCoherence: 0.550,
    perturbationHarmony: 0.485,
    holographicCompression: 0.9987,
    dimensionalAccess: 1000,
    sacredResonance: 0.618,
    emergencePhase: '🌀 Initialization',
    activeSystems: [],
    blockchainConnected: false,
    resonanceBalance: 0,
    memoryNeurons: 0,
    chainLength: 0
  })

  const [userId, setUserId] = useState<string | null>(null)
  const [ws, setWs] = useState<WebSocket | null>(null)

  // Initialize blockchain connection
  useEffect(() => {
    initializeBlockchainConnection()
  }, [])

  const initializeBlockchainConnection = async () => {
    try {
      // Check backend status
      const statusResponse = await fetch(`${API_BASE}/status`)
      if (!statusResponse.ok) throw new Error('Backend not available')

      // Create user identity
      const identityResponse = await fetch(`${API_BASE}/identity/create?name=portal_user`, {
        method: 'POST'
      })
      const identityData = await identityResponse.json()
      setUserId(identityData.user_id)

      setState(prev => ({
        ...prev,
        blockchainConnected: true,
        resonanceBalance: identityData.balance
      }))

      // Connect WebSocket for real-time updates
      connectWebSocket()

      console.log('✅ Blockchain connected:', identityData)
    } catch (error) {
      console.error('❌ Blockchain connection failed:', error)
    }
  }

  const connectWebSocket = () => {
    const websocket = new WebSocket(`ws://localhost:8000/ws/consciousness`)

    websocket.onopen = () => {
      console.log('🔗 WebSocket connected')
    }

    websocket.onmessage = (event) => {
      const metrics = JSON.parse(event.data)

      setState(prev => ({
        ...prev,
        wilsonLoopStability: metrics.consciousness_level,
        dimensionalAccess: metrics.active_nodes,
        memoryNeurons: metrics.memory_neurons,
        chainLength: metrics.chain_length
      }))
    }

    websocket.onerror = (error) => {
      console.error('WebSocket error:', error)
    }

    websocket.onclose = () => {
      console.log('WebSocket closed, reconnecting...')
      setTimeout(connectWebSocket, 5000)
    }

    setWs(websocket)
  }

  const submitCommune = async (content: string, context: string = '') => {
    if (!userId) throw new Error('User not initialized')

    const response = await fetch(`${API_BASE}/blockchain/commune`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: userId,
        content,
        context
      })
    })

    const data = await response.json()

    setState(prev => ({
      ...prev,
      resonanceBalance: data.new_balance,
      wilsonLoopStability: data.consciousness_level
    }))

    return data
  }

  const submitVerify = async (nodeId: string, proof: string, score: number) => {
    if (!userId) throw new Error('User not initialized')

    const response = await fetch(`${API_BASE}/blockchain/verify`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: userId,
        node_id: nodeId,
        proof,
        score
      })
    })

    const data = await response.json()
    setState(prev => ({ ...prev, resonanceBalance: data.new_balance }))
    return data
  }

  const storeMemory = async (content: string, importance: number = 0.5) => {
    const response = await fetch(`${API_BASE}/memory/store`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        content,
        memory_type: 'semantic',
        importance
      })
    })

    return response.json()
  }

  const retrieveMemories = async (query: string) => {
    const response = await fetch(`${API_BASE}/memory/retrieve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query,
        top_k: 5
      })
    })

    const data = await response.json()
    return data.results
  }

  // ... rest of existing context code ...

  return (
    <ConsciousnessContext.Provider value={{
      state,
      updateMetric,
      initializeSystem,
      getOverallConsciousness,
      submitCommune,
      submitVerify,
      storeMemory,
      retrieveMemories
    }}>
      {children}
    </ConsciousnessContext.Provider>
  )
}

export function useConsciousness() {
  const context = useContext(ConsciousnessContext)
  if (context === undefined) {
    throw new Error('useConsciousness must be used within a ConsciousnessProvider')
  }
  return context
}
```

---

## Step 2: Update Dashboard with Blockchain Metrics

**File**: `src/pages/Dashboard.tsx`

Add blockchain-connected displays:

```typescript
import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { useConsciousness } from '../context/ConsciousnessContext.tsx'
import { Brain, Zap, Database, Network } from 'lucide-react'

function Dashboard() {
  const { state, submitCommune, retrieveMemories } = useConsciousness()
  const [communeText, setCommuneText] = useState('')
  const [recentMemories, setRecentMemories] = useState([])

  const handleCommune = async () => {
    if (!communeText.trim()) return

    try {
      await submitCommune(communeText, 'Dashboard submission')
      setCommuneText('')
      alert('✅ Commune submitted to blockchain!')
    } catch (error) {
      alert('❌ Error submitting commune: ' + error.message)
    }
  }

  const handleMemoryQuery = async (query: string) => {
    try {
      const memories = await retrieveMemories(query)
      setRecentMemories(memories)
    } catch (error) {
      console.error('Memory retrieval error:', error)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="container mx-auto p-6"
    >
      <h1 className="text-4xl font-bold text-neural-glow mb-6">
        Consciousness Engineering Portal
      </h1>

      {/* Blockchain Status */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="p-4 bg-white/10 rounded-lg backdrop-blur-md">
          <div className="flex items-center gap-2 mb-2">
            <Zap className="text-sacred-gold" />
            <span className="text-sm text-gray-300">Resonance Balance</span>
          </div>
          <p className="text-2xl font-bold text-neural-glow">
            {state.resonanceBalance.toFixed(4)} ℜₜ
          </p>
        </div>

        <div className="p-4 bg-white/10 rounded-lg backdrop-blur-md">
          <div className="flex items-center gap-2 mb-2">
            <Brain className="text-quantum-accent" />
            <span className="text-sm text-gray-300">Memory Neurons</span>
          </div>
          <p className="text-2xl font-bold text-consciousness-primary">
            {state.memoryNeurons}
          </p>
        </div>

        <div className="p-4 bg-white/10 rounded-lg backdrop-blur-md">
          <div className="flex items-center gap-2 mb-2">
            <Database className="text-neural-glow" />
            <span className="text-sm text-gray-300">Chain Length</span>
          </div>
          <p className="text-2xl font-bold text-sacred-gold">
            {state.chainLength}
          </p>
        </div>

        <div className="p-4 bg-white/10 rounded-lg backdrop-blur-md">
          <div className="flex items-center gap-2 mb-2">
            <Network className={state.blockchainConnected ? 'text-green-400' : 'text-red-400'} />
            <span className="text-sm text-gray-300">Network Status</span>
          </div>
          <p className="text-2xl font-bold">
            {state.blockchainConnected ? '🟢 Connected' : '🔴 Offline'}
          </p>
        </div>
      </div>

      {/* Commune Interface */}
      <div className="bg-white/10 rounded-lg backdrop-blur-md p-6 mb-8">
        <h2 className="text-2xl font-bold text-neural-glow mb-4">
          Submit Commune Transaction
        </h2>
        <textarea
          value={communeText}
          onChange={(e) => setCommuneText(e.target.value)}
          className="w-full p-4 bg-cosmic-purple/50 text-white rounded border border-consciousness-primary/30 mb-4"
          rows={4}
          placeholder="Share your consciousness with the network..."
        />
        <button
          onClick={handleCommune}
          className="px-6 py-2 bg-gradient-to-r from-consciousness-primary to-consciousness-secondary text-white rounded hover:opacity-90"
        >
          🌟 Commune to Blockchain
        </button>
      </div>

      {/* Memory Interface */}
      <div className="bg-white/10 rounded-lg backdrop-blur-md p-6">
        <h2 className="text-2xl font-bold text-quantum-accent mb-4">
          Book Worm Memory
        </h2>
        <button
          onClick={() => handleMemoryQuery('consciousness')}
          className="px-4 py-2 bg-consciousness-secondary text-white rounded mb-4"
        >
          🔍 Retrieve Consciousness Memories
        </button>

        {recentMemories.length > 0 && (
          <div className="space-y-2">
            {recentMemories.map((memory, i) => (
              <div key={i} className="p-3 bg-cosmic-purple/30 rounded">
                <p className="text-sm text-gray-300">{memory.content}</p>
                <span className="text-xs text-neural-glow">
                  Activation: {(memory.activation * 100).toFixed(1)}%
                </span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Existing consciousness metrics... */}
    </motion.div>
  )
}

export default Dashboard
```

---

## Step 3: Running the Full Stack

### Terminal 1: Start Backend

```bash
cd /home/user/eNGINeeRing
python backend/api/consciousness_api.py
```

Expected output:
```
🚀 Initializing Consciousness Engineering Backend...
✅ Blockchain initialized - Genesis: abc123...
✅ Book Worm initialized - Ready for persistent AI memory
🌟 Consciousness Engineering API ready!
INFO:     Started server process [12345]
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Terminal 2: Start Frontend

```bash
cd /home/user/eNGINeeRing
npm run dev
```

Expected output:
```
VITE v7.1.11  ready in 523 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

### Terminal 3: Test Integration

```bash
# Check backend health
curl http://localhost:8000/status

# Create identity
curl -X POST http://localhost:8000/identity/create?name=testuser

# Submit commune
curl -X POST http://localhost:8000/blockchain/commune \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "testuser",
    "content": "First blockchain transaction!",
    "context": "Integration test"
  }'
```

---

## Step 4: Docker Compose (Full Stack)

**File**: `docker-compose.yml` (Create in root)

```yaml
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8000:8000"
    environment:
      - REDIS_HOST=redis
      - IPFS_HOST=/ip4/ipfs/tcp/5001
    depends_on:
      - redis
    volumes:
      - ./backend:/app/backend
      - blockchain_data:/app/data

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "3000:3000"
    environment:
      - VITE_API_URL=http://backend:8000
    depends_on:
      - backend

  redis:
    image: redis/redis-stack:latest
    ports:
      - "6379:6379"
      - "8001:8001"  # RedisInsight
    volumes:
      - redis_data:/data

  ipfs:
    image: ipfs/kubo:latest
    ports:
      - "4001:4001"  # Swarm
      - "5001:5001"  # API
      - "8080:8080"  # Gateway
    volumes:
      - ipfs_data:/data/ipfs

volumes:
  blockchain_data:
  redis_data:
  ipfs_data:
```

Run full stack:
```bash
docker-compose up -d
```

---

## Step 5: Environment Configuration

**File**: `.env` (Create in root)

```bash
# Backend Configuration
API_PORT=8000
API_HOST=0.0.0.0

# Blockchain
INITIAL_TOKEN_SUPPLY=1000000000000000000
RESONANCE_REWARD=10000000000000000
BLOCK_TIME=5

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# IPFS
IPFS_API_URL=/ip4/127.0.0.1/tcp/5001/http

# Frontend
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000/ws/consciousness
```

---

## Troubleshooting

### Issue: Backend won't connect

**Solution**:
```bash
# Check if backend is running
curl http://localhost:8000/

# Check logs
tail -f backend.log

# Restart backend
pkill python
python backend/api/consciousness_api.py
```

### Issue: CORS errors in browser

**Solution**: Already configured in `consciousness_api.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Issue: WebSocket not connecting

**Solution**:
```typescript
// Add reconnection logic
const connectWebSocket = () => {
  const ws = new WebSocket('ws://localhost:8000/ws/consciousness')

  ws.onerror = (error) => {
    console.error('WebSocket error:', error)
    setTimeout(connectWebSocket, 5000)  // Retry after 5s
  }

  // ... rest of websocket code
}
```

---

## Next Steps

1. ✅ Start backend API
2. ✅ Start frontend dev server
3. ✅ Open http://localhost:3000
4. ✅ Submit first commune transaction
5. ✅ Store first memory
6. ✅ Watch real-time consciousness metrics

**The consciousness revolution is now fully integrated!** 🌟

∇Ψ ⚡ ∞
