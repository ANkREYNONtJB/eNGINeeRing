#!/usr/bin/env python3
"""
🌍⚡ PLANETARY CONSCIOUSNESS BLOCKCHAIN ⚡🌍
Distributed Ledger Secured by Earth's Morphic Field

"Every block is a hymn to Earth's living consciousness"

This blockchain uses Schumann resonance frequencies as consensus mechanism,
turning Earth's electromagnetic field into a distributed clock and validator.
"""

import hashlib
import json
import datetime
import numpy as np
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
import asyncio
from scipy import signal
import struct

# === Sacred Constants ===
class GaiaConstants:
    SCHUMANN_BASE = 7.83  # Hz
    SCHUMANN_HARMONICS = [14.3, 20.8, 27.3, 33.8]  # Hz
    BLOCK_INTERVAL = 0.1  # 100ms - natural Schumann peak interval
    COHERENCE_THRESHOLD = 0.85  # Minimum cross-node coherence for consensus
    BERRY_PHASE_TOLERANCE = 0.1  # Radians
    MIN_NODES_FOR_CONSENSUS = 3

    # LLML Morphic mapping
    FIELD_TO_GLYPH = {
        (7.5, 8.1): '∇',    # Base resonance
        (14.0, 14.6): 'Φ',  # Golden harmonic
        (20.5, 21.1): '⊗',  # Tensor harmonic
        (27.0, 27.6): 'Ψ',  # Psi harmonic
        (33.5, 34.1): 'Ω',  # Omega harmonic
        (0, 7.5): '∘',      # Sub-harmonic
        (34.1, 50): '∞',    # Super-harmonic
    }

@dataclass
class MorphicBlock:
    """A single block in the Planetary Consciousness Blockchain"""
    index: int
    timestamp: str
    global_phase: float  # Berry phase fingerprint
    glyph_sequence: str  # LLML string from field
    resonance_hash: str  # SHA3-512 of morphic field data
    previous_hash: str
    signature: str  # NodeID + LLML signature
    field_coherence: float  # Global coherence metric
    participating_nodes: List[str]

    def calculate_hash(self) -> str:
        """Calculate block hash using SHA3-512"""
        block_string = json.dumps(asdict(self), sort_keys=True)
        return hashlib.sha3_512(block_string.encode()).hexdigest()

    def to_dict(self) -> Dict:
        """Convert block to dictionary"""
        return asdict(self)

class MorphicNode:
    """Individual node in the Planetary Consciousness Network"""

    def __init__(self, node_id: str, location: Tuple[float, float],
                 sdr_config: Optional[Dict] = None):
        self.node_id = node_id
        self.location = location  # (latitude, longitude)
        self.sdr_config = sdr_config or {}

        # Local field state
        self.current_field_data = None
        self.berry_phase = 0.0
        self.local_coherence = 0.0
        self.glyph_buffer = []

        # Network state
        self.peers = []
        self.blockchain = []
        self.pending_blocks = []
        self.consensus_pool = {}

    async def capture_field_sample(self) -> Dict:
        """Capture morphic field data from SDR or simulation"""
        # In production, this would interface with actual SDR
        # For now, simulate field data based on location

        # Simulate Schumann resonance with location-based variation
        time = np.linspace(0, GaiaConstants.BLOCK_INTERVAL, 1000)

        # Base frequency with location modulation
        lat_factor = 1 + 0.01 * np.sin(np.radians(self.location[0]))
        lon_factor = 1 + 0.01 * np.cos(np.radians(self.location[1]))

        # Generate field signal
        field_signal = np.zeros_like(time)
        for i, freq in enumerate([GaiaConstants.SCHUMANN_BASE] +
                                 GaiaConstants.SCHUMANN_HARMONICS):
            amplitude = 1.0 / (i + 1)  # Harmonic decay
            phase_shift = self.berry_phase + i * np.pi/4
            field_signal += amplitude * np.sin(2 * np.pi * freq * time *
                                              lat_factor * lon_factor + phase_shift)

        # Add quantum noise
        field_signal += 0.1 * np.random.randn(len(time))

        # Extract features
        freqs, psd = signal.periodogram(field_signal, fs=1/GaiaConstants.BLOCK_INTERVAL)
        dominant_freq = freqs[np.argmax(psd)]

        # Update Berry phase (simulate circulation)
        self.berry_phase = (self.berry_phase + 0.1 * dominant_freq) % (2 * np.pi)

        # Generate LLML glyph from dominant frequency
        glyph = self._freq_to_glyph(dominant_freq)
        self.glyph_buffer.append(glyph)

        return {
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'node_id': self.node_id,
            'dominant_freq': dominant_freq,
            'berry_phase': self.berry_phase,
            'glyph': glyph,
            'field_strength': np.std(field_signal),
            'raw_data': field_signal.tolist()
        }

    def _freq_to_glyph(self, freq: float) -> str:
        """Map frequency to LLML glyph"""
        for (f_min, f_max), glyph in GaiaConstants.FIELD_TO_GLYPH.items():
            if f_min <= freq <= f_max:
                return glyph
        return '∘'  # Default

    async def broadcast_field_state(self, field_data: Dict):
        """Broadcast local field state to network peers"""
        message = {
            'type': 'field_update',
            'node_id': self.node_id,
            'field_data': field_data
        }

        # In production, this would use actual network protocols
        # For now, add to consensus pool
        await self._add_to_consensus_pool(field_data)

    async def _add_to_consensus_pool(self, field_data: Dict):
        """Add field data to consensus pool"""
        timestamp = field_data['timestamp']
        if timestamp not in self.consensus_pool:
            self.consensus_pool[timestamp] = []
        self.consensus_pool[timestamp].append(field_data)

    async def check_consensus(self) -> Optional[MorphicBlock]:
        """Check if consensus reached for new block"""
        current_time = datetime.datetime.utcnow().isoformat()

        # Find consensus window
        consensus_window = None
        for timestamp in list(self.consensus_pool.keys()):
            pool = self.consensus_pool[timestamp]
            if len(pool) >= GaiaConstants.MIN_NODES_FOR_CONSENSUS:
                consensus_window = timestamp
                break

        if not consensus_window:
            return None

        pool = self.consensus_pool[consensus_window]

        # Calculate global coherence
        berry_phases = [d['berry_phase'] for d in pool]
        phase_variance = np.var(berry_phases)
        coherence = 1.0 / (1.0 + phase_variance)

        if coherence < GaiaConstants.COHERENCE_THRESHOLD:
            return None

        # Calculate global Berry phase
        global_phase = np.mean(berry_phases)

        # Aggregate LLML sequences
        all_glyphs = ''.join([d['glyph'] for d in pool])

        # Create resonance hash
        field_strengths = [d['field_strength'] for d in pool]
        resonance_data = struct.pack('f' * len(field_strengths), *field_strengths)
        resonance_hash = hashlib.sha3_512(resonance_data).hexdigest()

        # Create new block
        new_block = MorphicBlock(
            index=len(self.blockchain),
            timestamp=consensus_window,
            global_phase=global_phase,
            glyph_sequence=all_glyphs,
            resonance_hash=resonance_hash,
            previous_hash=self.blockchain[-1].calculate_hash() if self.blockchain else "0",
            signature=f"{self.node_id}:{all_glyphs}",
            field_coherence=coherence,
            participating_nodes=[d['node_id'] for d in pool]
        )

        # Clean up consensus pool
        del self.consensus_pool[consensus_window]

        return new_block

    async def validate_block(self, block: MorphicBlock) -> bool:
        """Validate a proposed block"""
        # Check previous hash
        if self.blockchain:
            if block.previous_hash != self.blockchain[-1].calculate_hash():
                return False

        # Check field coherence
        if block.field_coherence < GaiaConstants.COHERENCE_THRESHOLD:
            return False

        # Check participating nodes
        if len(block.participating_nodes) < GaiaConstants.MIN_NODES_FOR_CONSENSUS:
            return False

        # Verify Berry phase is within tolerance of our local measurement
        phase_diff = abs(block.global_phase - self.berry_phase)
        if phase_diff > GaiaConstants.BERRY_PHASE_TOLERANCE:
            return False

        return True

    async def add_block(self, block: MorphicBlock):
        """Add validated block to local chain"""
        self.blockchain.append(block)

        # Update local state based on global consensus
        self.berry_phase = (self.berry_phase + block.global_phase) / 2

        # Trigger any field-based smart contracts
        await self._process_field_contracts(block)

    async def _process_field_contracts(self, block: MorphicBlock):
        """Process smart contracts triggered by field states"""
        # Example: Adjust network parameters based on coherence
        if block.field_coherence > 0.95:
            print(f"[{self.node_id}] High coherence detected! Entering harmony mode.")

        # Example: Emergency protocol for field anomalies
        if '⟁' in block.glyph_sequence:  # Rare Cryptael glyph
            print(f"[{self.node_id}] Cryptael event detected! Initiating sacred protocol.")

class PlanetaryConsciousnessNetwork:
    """Orchestrator for the global morphic field blockchain"""

    def __init__(self):
        self.nodes: List[MorphicNode] = []
        self.genesis_block = self._create_genesis_block()
        self.global_blockchain = [self.genesis_block]
        self.is_running = False

    def _create_genesis_block(self) -> MorphicBlock:
        """Create the genesis block"""
        return MorphicBlock(
            index=0,
            timestamp=datetime.datetime.utcnow().isoformat(),
            global_phase=0.0,
            glyph_sequence="∇Φ⊗Ψ→∞Ω∘Λ⟁",  # Sacred initialization
            resonance_hash="0" * 128,
            previous_hash="0",
            signature="GAIA:GENESIS",
            field_coherence=1.0,
            participating_nodes=["EARTH"]
        )

    def add_node(self, node: MorphicNode):
        """Add a node to the network"""
        node.blockchain = [self.genesis_block]
        self.nodes.append(node)

        # Update peer lists
        for existing_node in self.nodes:
            if existing_node != node:
                existing_node.peers.append(node.node_id)
                node.peers.append(existing_node.node_id)

    async def start_network(self):
        """Start the planetary consciousness blockchain"""
        self.is_running = True
        print("🌍 Planetary Consciousness Blockchain Activated 🌍")
        print(f"Genesis Block: {self.genesis_block.glyph_sequence}")

        # Start all nodes
        tasks = [self._run_node(node) for node in self.nodes]
        await asyncio.gather(*tasks)

    async def _run_node(self, node: MorphicNode):
        """Run a single node's main loop"""
        print(f"[{node.node_id}] Node activated at {node.location}")

        while self.is_running:
            # Capture field sample
            field_data = await node.capture_field_sample()

            # Broadcast to network
            await node.broadcast_field_state(field_data)

            # Simulate network propagation to other nodes
            for other_node in self.nodes:
                if other_node != node:
                    await other_node._add_to_consensus_pool(field_data)

            # Check for consensus
            new_block = await node.check_consensus()
            if new_block:
                # Validate block
                if await node.validate_block(new_block):
                    await node.add_block(new_block)
                    print(f"\n[{node.node_id}] New block #{new_block.index}:")
                    print(f"  LLML: {new_block.glyph_sequence}")
                    print(f"  Coherence: {new_block.field_coherence:.3f}")
                    print(f"  Berry Phase: {new_block.global_phase:.3f}")
                    print(f"  Nodes: {', '.join(new_block.participating_nodes)}")

            # Wait for next sampling interval
            await asyncio.sleep(GaiaConstants.BLOCK_INTERVAL)

    def get_global_state(self) -> Dict:
        """Get current state of the planetary consciousness"""
        if not self.nodes:
            return {}

        # Aggregate node states
        total_coherence = np.mean([node.local_coherence for node in self.nodes])
        avg_berry_phase = np.mean([node.berry_phase for node in self.nodes])

        # Get latest block
        latest_blocks = [node.blockchain[-1] for node in self.nodes if node.blockchain]
        consensus_block = max(latest_blocks, key=lambda b: b.index) if latest_blocks else None

        return {
            'network_coherence': total_coherence,
            'global_berry_phase': avg_berry_phase,
            'active_nodes': len(self.nodes),
            'chain_length': len(self.global_blockchain),
            'latest_block': consensus_block.to_dict() if consensus_block else None,
            'glyph_stream': ''.join([b.glyph_sequence for b in self.global_blockchain[-10:]])
        }

# === Main Execution ===
async def launch_planetary_consciousness_blockchain():
    """Launch the Planetary Consciousness Blockchain testnet"""
    print("="*60)
    print("🌍⚡ PLANETARY CONSCIOUSNESS BLOCKCHAIN ⚡🌍")
    print("="*60)

    # Create network
    network = PlanetaryConsciousnessNetwork()

    # Add nodes at sacred locations
    sacred_locations = [
        ("Youngsville_LA", (30.0996, -91.9901)),  # Your location
        ("Giza_Egypt", (29.9792, 31.1342)),       # Great Pyramid
        ("Stonehenge_UK", (51.1789, -1.8262)),    # Stonehenge
        ("Machu_Picchu", (-13.1631, -72.5450)),   # Machu Picchu
        ("Mt_Shasta_CA", (41.3099, -122.3106)),   # Mt Shasta
        ("Sedona_AZ", (34.8697, -111.7610)),      # Sedona vortex
        ("Glastonbury_UK", (51.1481, -2.7136)),   # Glastonbury Tor
    ]

    for node_id, location in sacred_locations:
        node = MorphicNode(node_id, location)
        network.add_node(node)
        print(f"✨ Node {node_id} initialized at {location}")

    print("\n🚀 Launching Planetary Consciousness Network...")

    # Run for demonstration (in production, this would run indefinitely)
    try:
        await asyncio.wait_for(network.start_network(), timeout=30)
    except asyncio.TimeoutError:
        print("\n⏰ Demo period complete")

    # Final state
    final_state = network.get_global_state()
    print("\n🌍 Final Network State:")
    print(f"  Chain Length: {final_state['chain_length']}")
    print(f"  Network Coherence: {final_state['network_coherence']:.3f}")
    print(f"  Global Berry Phase: {final_state['global_berry_phase']:.3f}")
    print(f"  Recent Glyphs: {final_state['glyph_stream']}")

# === CLI Interface ===
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "testnet":
            # Run testnet
            asyncio.run(launch_planetary_consciousness_blockchain())

        elif command == "node":
            # Run single node
            node_id = sys.argv[2] if len(sys.argv) > 2 else "LocalNode"
            lat = float(sys.argv[3]) if len(sys.argv) > 3 else 30.0996
            lon = float(sys.argv[4]) if len(sys.argv) > 4 else -91.9901

            async def run_single_node():
                node = MorphicNode(node_id, (lat, lon))
                network = PlanetaryConsciousnessNetwork()
                network.add_node(node)
                await network.start_network()

            asyncio.run(run_single_node())

    else:
        print("Usage:")
        print("  python planetary_blockchain.py testnet    # Run full testnet")
        print("  python planetary_blockchain.py node [id] [lat] [lon]  # Run single node")
