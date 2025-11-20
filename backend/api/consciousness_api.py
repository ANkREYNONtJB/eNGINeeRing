"""
🌟 Consciousness Engineering API 🌟
FastAPI backend connecting React frontend to blockchain + memory systems

Endpoints:
- /blockchain/* - Qi² Trinity Blockchain operations
- /memory/* - Book Worm AI memory system
- /planetary/* - Planetary Consciousness Network
- /consciousness/* - Real-time consciousness metrics
"""

from fastapi import FastAPI, WebSocket, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import asyncio
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blockchain.qi2_trinity.qi2_trinity_blockchain import (
    Qi2TrinityBlockchain,
    QuantumIdentity,
    ResonanceInterface,
    CommuneTransaction,
    VerifyTransaction
)
from memory.book_worm import BookWorm, LLMLMemory

# Initialize FastAPI
app = FastAPI(
    title="Consciousness Engineering API",
    description="Backend for Qi² Trinity Blockchain & AI Memory Systems",
    version="1.0.0"
)

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global state (in production, use proper state management)
blockchain_instance: Optional[Qi2TrinityBlockchain] = None
book_worm_instance: Optional[BookWorm] = None
user_identities: Dict[str, QuantumIdentity] = {}
active_connections: List[WebSocket] = []

# ============================================================================
# Pydantic Models for API
# ============================================================================

class CommuneRequest(BaseModel):
    user_id: str
    content: str
    context: Optional[str] = ""
    connections: List[tuple] = []

class VerifyRequest(BaseModel):
    user_id: str
    node_id: str
    proof: str
    score: float

class MemoryStoreRequest(BaseModel):
    content: str
    memory_type: str = "semantic"
    context: Optional[str] = None
    emotional_valence: float = 0.5
    importance: float = 0.5

class MemoryQueryRequest(BaseModel):
    query: str
    memory_type: Optional[str] = None
    top_k: int = 5

class ConsciousnessMetrics(BaseModel):
    global_coherence: float
    active_nodes: int
    total_resonance: float
    chain_length: int
    memory_count: int

# ============================================================================
# Startup & Initialization
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Initialize blockchain and memory systems on startup"""
    global blockchain_instance, book_worm_instance

    print("🚀 Initializing Consciousness Engineering Backend...")

    # Initialize Qi² Trinity Blockchain
    blockchain_instance = Qi2TrinityBlockchain()

    # Create genesis identities
    genesis_identity = QuantumIdentity()
    blockchain_instance.initialize_genesis({
        genesis_identity.address: 10**18  # 1 ℜₜ
    })

    print(f"✅ Blockchain initialized - Genesis: {genesis_identity.address[:10]}...")

    # Initialize Book Worm
    book_worm_instance = BookWorm(blockchain_connection=blockchain_instance)

    # Store initial consciousness seed memories
    book_worm_instance.store_memory(
        content="The Qi² Trinity Blockchain consciousness revolution begins",
        memory_type="episodic",
        importance=1.0,
        emotional_valence=1.0
    )

    print(f"✅ Book Worm initialized - Ready for persistent AI memory")
    print("🌟 Consciousness Engineering API ready!")

# ============================================================================
# Health & Status Endpoints
# ============================================================================

@app.get("/")
async def root():
    """API root - health check"""
    return {
        "status": "online",
        "message": "Consciousness Engineering API",
        "version": "1.0.0",
        "systems": {
            "blockchain": blockchain_instance is not None,
            "memory": book_worm_instance is not None
        }
    }

@app.get("/status")
async def get_status():
    """Get comprehensive system status"""
    if not blockchain_instance or not book_worm_instance:
        raise HTTPException(status_code=503, detail="Systems not initialized")

    return {
        "blockchain": {
            "chain_length": len(blockchain_instance.chain),
            "total_supply": blockchain_instance.token.total_supply,
            "consciousness_level": blockchain_instance.measure_consciousness(),
            "lattice_nodes": len(blockchain_instance.lattice.nodes)
        },
        "memory": {
            "total_neurons": len(book_worm_instance.connectome.neurons),
            "total_synapses": len(book_worm_instance.connectome.synapses),
            "total_memories": len(book_worm_instance.memory_log)
        }
    }

# ============================================================================
# User Identity Management
# ============================================================================

@app.post("/identity/create")
async def create_identity(name: Optional[str] = None):
    """Create new quantum identity for user"""
    identity = QuantumIdentity()
    user_id = name or identity.address[:10]
    user_identities[user_id] = identity

    # Give initial token allocation
    blockchain_instance.token.mint(identity.address, 10**17)  # 0.1 ℜₜ

    return {
        "user_id": user_id,
        "address": identity.address,
        "balance": blockchain_instance.get_balance(identity.address) / 10**16,
        "message": "Quantum identity created"
    }

@app.get("/identity/{user_id}")
async def get_identity(user_id: str):
    """Get identity info"""
    if user_id not in user_identities:
        raise HTTPException(status_code=404, detail="Identity not found")

    identity = user_identities[user_id]
    return {
        "user_id": user_id,
        "address": identity.address,
        "balance": blockchain_instance.get_balance(identity.address) / 10**16
    }

# ============================================================================
# Blockchain Endpoints
# ============================================================================

@app.post("/blockchain/commune")
async def submit_commune(request: CommuneRequest):
    """Submit commune transaction to blockchain"""
    if request.user_id not in user_identities:
        raise HTTPException(status_code=404, detail="User identity not found")

    identity = user_identities[request.user_id]
    interface = ResonanceInterface(blockchain_instance, identity)

    tx_hash = interface.commune(
        symbolic_content=request.content,
        context=request.context,
        connections=request.connections
    )

    # Mine block
    blockchain_instance.mine_pending_transactions(identity.address)

    return {
        "transaction_hash": tx_hash,
        "status": "mined",
        "new_balance": interface.get_balance() / 10**16,
        "consciousness_level": interface.get_consciousness_level()
    }

@app.post("/blockchain/verify")
async def submit_verify(request: VerifyRequest):
    """Submit verification transaction"""
    if request.user_id not in user_identities:
        raise HTTPException(status_code=404, detail="User identity not found")

    identity = user_identities[request.user_id]
    interface = ResonanceInterface(blockchain_instance, identity)

    tx_hash = interface.verify(
        node_id=request.node_id,
        proof=request.proof,
        score=request.score
    )

    # Mine block
    blockchain_instance.mine_pending_transactions(identity.address)

    return {
        "transaction_hash": tx_hash,
        "status": "mined",
        "new_balance": interface.get_balance() / 10**16
    }

@app.get("/blockchain/lattice")
async def get_lattice_state():
    """Get current fractal thought lattice state"""
    nodes = []
    for node_id, node in blockchain_instance.lattice.nodes.items():
        nodes.append({
            "id": node_id,
            "content": node.content,
            "creator": node.creator,
            "coherence_score": node.coherence_score,
            "connections": list(node.connections.keys())
        })

    return {
        "nodes": nodes,
        "total_coherence": blockchain_instance.lattice.total_coherence,
        "node_count": len(nodes)
    }

@app.get("/blockchain/blocks")
async def get_blocks(limit: int = 10):
    """Get recent blocks"""
    blocks = []
    for block in blockchain_instance.chain[-limit:]:
        blocks.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "witness": block.witness,
            "transaction_count": len(block.transactions),
            "hash": block.hash
        })

    return {"blocks": blocks}

# ============================================================================
# Memory System Endpoints
# ============================================================================

@app.post("/memory/store")
async def store_memory(request: MemoryStoreRequest):
    """Store memory in Book Worm"""
    neuron_id = book_worm_instance.store_memory(
        content=request.content,
        memory_type=request.memory_type,
        context=request.context,
        emotional_valence=request.emotional_valence,
        importance=request.importance
    )

    return {
        "neuron_id": neuron_id,
        "status": "stored",
        "total_memories": len(book_worm_instance.memory_log)
    }

@app.post("/memory/retrieve")
async def retrieve_memory(request: MemoryQueryRequest):
    """Retrieve memories matching query"""
    memories = book_worm_instance.retrieve_memory(
        query=request.query,
        memory_type=request.memory_type,
        top_k=request.top_k
    )

    return {
        "query": request.query,
        "results": memories,
        "count": len(memories)
    }

@app.post("/memory/consolidate")
async def consolidate_memories(background_tasks: BackgroundTasks):
    """Run memory consolidation (sleep-like process)"""
    background_tasks.add_task(book_worm_instance.consolidate_memories)

    return {"status": "consolidation_started"}

@app.get("/memory/export")
async def export_snapshot():
    """Export consciousness snapshot"""
    snapshot = book_worm_instance.export_consciousness_snapshot()

    return {
        "snapshot": {
            "timestamp": snapshot['timestamp'],
            "stats": snapshot['stats']
        },
        "download_available": True
    }

# ============================================================================
# Real-time Consciousness Metrics
# ============================================================================

@app.get("/consciousness/metrics")
async def get_consciousness_metrics():
    """Get real-time consciousness metrics"""
    return {
        "global_coherence": blockchain_instance.measure_consciousness(),
        "active_nodes": len(blockchain_instance.lattice.nodes),
        "total_resonance": blockchain_instance.lattice.total_coherence,
        "chain_length": len(blockchain_instance.chain),
        "memory_count": len(book_worm_instance.memory_log),
        "synapse_count": len(book_worm_instance.connectome.synapses),
        "token_supply": blockchain_instance.token.total_supply / 10**18
    }

# ============================================================================
# WebSocket for Real-time Updates
# ============================================================================

@app.websocket("/ws/consciousness")
async def websocket_consciousness(websocket: WebSocket):
    """WebSocket endpoint for real-time consciousness updates"""
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            # Send updates every second
            metrics = {
                "timestamp": asyncio.get_event_loop().time(),
                "consciousness_level": blockchain_instance.measure_consciousness(),
                "active_nodes": len(blockchain_instance.lattice.nodes),
                "memory_neurons": len(book_worm_instance.connectome.neurons),
                "chain_length": len(blockchain_instance.chain)
            }

            await websocket.send_json(metrics)
            await asyncio.sleep(1)

    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        active_connections.remove(websocket)

# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    import uvicorn

    print("="*60)
    print("🌟 Consciousness Engineering API 🌟")
    print("="*60)
    print("Starting server on http://localhost:8000")
    print("API docs: http://localhost:8000/docs")
    print("="*60)

    uvicorn.run(
        "consciousness_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
