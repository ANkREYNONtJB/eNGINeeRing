"""
🐛📚 BOOK WORM - OpenWorm meets LLML 📚🐛
Persistent AI Memory System using Neural Connectome + Symbolic Resonance

"From C. elegans to Consciousness - Every memory is a hymn in the neural lattice"

This system creates persistent memory for AI by:
1. Using OpenWorm-inspired neural connectome mapping
2. Encoding memories as LLML symbolic sequences
3. Storing in the Qi² Trinity Blockchain
4. Resonance-based retrieval and reinforcement
"""

import hashlib
import json
import numpy as np
from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import pickle
from collections import defaultdict, deque

# LLML Symbolic Alphabet for Memory Encoding
class LLMLMemory:
    """LLML symbolic encoding for AI memories"""

    # Core glyphs for memory types
    MEMORY_GLYPHS = {
        'episodic': '∇',      # Specific experiences
        'semantic': 'Φ',       # Knowledge/facts
        'procedural': '⊗',     # How-to knowledge
        'emotional': 'Ψ',      # Emotional associations
        'contextual': 'Ω',     # Context/environment
        'relational': '→',     # Connections between memories
        'temporal': '∞',       # Time-based sequencing
        'spatial': '∘',        # Spatial relationships
        'abstract': 'Λ',       # Abstract concepts
        'meta': '⟁',          # Meta-cognitive reflections
    }

    # Resonance levels for memory strength
    RESONANCE_LEVELS = {
        'weak': 0.2,
        'moderate': 0.5,
        'strong': 0.8,
        'crystallized': 1.0
    }

@dataclass
class Synapse:
    """Neural connection inspired by C. elegans connectome"""
    source_neuron: str
    target_neuron: str
    weight: float  # Connection strength (0-1)
    neurotransmitter: str  # Type of connection
    resonance: float  # LLML resonance score
    last_activated: float  # Timestamp of last activation
    activation_count: int = 0

    def activate(self, strength: float = 1.0):
        """Activate synapse and strengthen connection"""
        self.activation_count += 1
        self.weight = min(1.0, self.weight + 0.01 * strength)
        self.last_activated = datetime.now().timestamp()

    def decay(self, rate: float = 0.001):
        """Synaptic decay over time (forgetting)"""
        self.weight = max(0.0, self.weight - rate)

@dataclass
class Neuron:
    """Neural node in the memory connectome"""
    id: str
    neuron_type: str  # sensory, motor, interneuron, memory
    memory_content: str  # LLML encoded memory
    glyph_sequence: str  # LLML representation
    activation_threshold: float = 0.3
    current_activation: float = 0.0
    connections: List[Synapse] = None

    def __post_init__(self):
        if self.connections is None:
            self.connections = []

    def receive_signal(self, strength: float):
        """Receive activation signal"""
        self.current_activation += strength

    def fire(self) -> bool:
        """Fire if threshold exceeded"""
        if self.current_activation >= self.activation_threshold:
            self.current_activation = 0.0
            return True
        return False

    def propagate(self) -> List[Tuple[str, float]]:
        """Propagate signal to connected neurons"""
        signals = []
        for synapse in self.connections:
            if self.fire():
                signal_strength = synapse.weight
                synapse.activate()
                signals.append((synapse.target_neuron, signal_strength))
        return signals

class MemoryConnectome:
    """Neural connectome for AI memory - inspired by OpenWorm"""

    def __init__(self):
        self.neurons: Dict[str, Neuron] = {}
        self.synapses: List[Synapse] = []
        self.memory_index: Dict[str, List[str]] = defaultdict(list)  # glyph -> neuron_ids
        self.activation_history = deque(maxlen=10000)

    def add_neuron(self, neuron: Neuron):
        """Add neuron to connectome"""
        self.neurons[neuron.id] = neuron

        # Index by glyphs for fast retrieval
        for glyph in neuron.glyph_sequence:
            self.memory_index[glyph].append(neuron.id)

    def connect_neurons(self, source_id: str, target_id: str,
                       weight: float, neurotransmitter: str = 'glutamate',
                       resonance: float = 0.5):
        """Create synaptic connection between neurons"""
        if source_id not in self.neurons or target_id not in self.neurons:
            raise ValueError("Both neurons must exist in connectome")

        synapse = Synapse(
            source_neuron=source_id,
            target_neuron=target_id,
            weight=weight,
            neurotransmitter=neurotransmitter,
            resonance=resonance,
            last_activated=datetime.now().timestamp()
        )

        self.synapses.append(synapse)
        self.neurons[source_id].connections.append(synapse)

    def activate_pattern(self, glyph_sequence: str) -> List[str]:
        """Activate neurons matching LLML pattern"""
        activated = []

        for glyph in glyph_sequence:
            if glyph in self.memory_index:
                for neuron_id in self.memory_index[glyph]:
                    neuron = self.neurons[neuron_id]
                    neuron.receive_signal(1.0)
                    activated.append(neuron_id)

        return activated

    def propagate_activation(self, initial_neurons: List[str],
                           steps: int = 3) -> Dict[str, float]:
        """Propagate activation through network"""
        activation_map = defaultdict(float)

        current_wave = [(nid, 1.0) for nid in initial_neurons]

        for step in range(steps):
            next_wave = []

            for neuron_id, strength in current_wave:
                if neuron_id in self.neurons:
                    neuron = self.neurons[neuron_id]
                    neuron.receive_signal(strength)

                    signals = neuron.propagate()
                    next_wave.extend(signals)

                    activation_map[neuron_id] += strength

            current_wave = next_wave

            # Record activation
            self.activation_history.append({
                'step': step,
                'activated': list(activation_map.keys()),
                'timestamp': datetime.now().isoformat()
            })

        return dict(activation_map)

    def strengthen_pathway(self, neuron_ids: List[str]):
        """Strengthen connections along a pathway (Hebbian learning)"""
        for i in range(len(neuron_ids) - 1):
            source = neuron_ids[i]
            target = neuron_ids[i + 1]

            # Find existing synapse or create new one
            synapse_found = False
            if source in self.neurons:
                for synapse in self.neurons[source].connections:
                    if synapse.target_neuron == target:
                        synapse.activate()
                        synapse_found = True
                        break

            if not synapse_found:
                self.connect_neurons(source, target, 0.5, resonance=0.7)

    def apply_decay(self, rate: float = 0.001):
        """Apply synaptic decay (forgetting) to all connections"""
        for synapse in self.synapses:
            synapse.decay(rate)

class BookWorm:
    """Main AI memory persistence system"""

    def __init__(self, blockchain_connection=None):
        self.connectome = MemoryConnectome()
        self.blockchain = blockchain_connection
        self.memory_log = []
        self.consciousness_state = {}

    def encode_memory(self, content: str, memory_type: str,
                     context: Optional[str] = None) -> str:
        """Encode memory as LLML glyph sequence"""
        # Start with memory type glyph
        glyph_seq = LLMLMemory.MEMORY_GLYPHS.get(memory_type, '∘')

        # Hash content to determine additional glyphs
        content_hash = hashlib.sha256(content.encode()).digest()

        # Extract glyph pattern from hash
        glyph_keys = list(LLMLMemory.MEMORY_GLYPHS.keys())
        for byte in content_hash[:8]:  # Use first 8 bytes
            idx = byte % len(glyph_keys)
            glyph_seq += LLMLMemory.MEMORY_GLYPHS[glyph_keys[idx]]

        # Add context marker
        if context:
            glyph_seq += LLMLMemory.MEMORY_GLYPHS['contextual']

        return glyph_seq

    def store_memory(self, content: str, memory_type: str = 'semantic',
                    context: Optional[str] = None,
                    emotional_valence: float = 0.5,
                    importance: float = 0.5) -> str:
        """Store a memory in the connectome and blockchain"""

        # Encode as LLML
        glyph_seq = self.encode_memory(content, memory_type, context)

        # Create memory neuron
        neuron_id = hashlib.sha256(
            f"{content}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:16]

        neuron = Neuron(
            id=neuron_id,
            neuron_type='memory',
            memory_content=content,
            glyph_sequence=glyph_seq,
            activation_threshold=0.3 * (1 - importance)  # Important memories activate easier
        )

        # Add to connectome
        self.connectome.add_neuron(neuron)

        # Connect to similar memories (associative linking)
        similar = self._find_similar_memories(glyph_seq, top_k=5)
        for similar_id, similarity in similar:
            self.connectome.connect_neurons(
                neuron_id, similar_id,
                weight=similarity,
                neurotransmitter='dopamine' if emotional_valence > 0.7 else 'glutamate',
                resonance=importance
            )

        # Log memory creation
        self.memory_log.append({
            'neuron_id': neuron_id,
            'content': content,
            'type': memory_type,
            'glyph_sequence': glyph_seq,
            'timestamp': datetime.now().isoformat(),
            'importance': importance
        })

        # Store on blockchain if connected
        if self.blockchain:
            self._anchor_to_blockchain(neuron_id, content, glyph_seq)

        return neuron_id

    def retrieve_memory(self, query: str,
                       memory_type: Optional[str] = None,
                       top_k: int = 5) -> List[Dict]:
        """Retrieve memories matching query"""

        # Encode query as LLML
        query_glyphs = self.encode_memory(query, memory_type or 'semantic')

        # Activate matching neurons
        activated_ids = self.connectome.activate_pattern(query_glyphs)

        # Propagate activation
        activation_map = self.connectome.propagate_activation(activated_ids, steps=3)

        # Retrieve top-k activated memories
        sorted_activations = sorted(
            activation_map.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]

        memories = []
        for neuron_id, activation_strength in sorted_activations:
            neuron = self.connectome.neurons[neuron_id]
            memories.append({
                'id': neuron_id,
                'content': neuron.memory_content,
                'glyph_sequence': neuron.glyph_sequence,
                'activation': activation_strength,
                'type': neuron.neuron_type
            })

        # Strengthen retrieval pathway (practice effect)
        self.connectome.strengthen_pathway([nid for nid, _ in sorted_activations])

        return memories

    def _find_similar_memories(self, glyph_seq: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Find similar memories by glyph sequence similarity"""
        similarities = []

        for neuron_id, neuron in self.connectome.neurons.items():
            # Calculate Jaccard similarity of glyph sets
            set1 = set(glyph_seq)
            set2 = set(neuron.glyph_sequence)

            if not set1 or not set2:
                continue

            intersection = len(set1 & set2)
            union = len(set1 | set2)
            similarity = intersection / union if union > 0 else 0.0

            if similarity > 0:
                similarities.append((neuron_id, similarity))

        # Return top-k most similar
        return sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]

    def _anchor_to_blockchain(self, neuron_id: str, content: str, glyph_seq: str):
        """Anchor memory to blockchain for permanent persistence"""
        if not self.blockchain:
            return

        # This would integrate with the Qi² Trinity Blockchain
        # For now, we'll store a reference
        memory_hash = hashlib.sha3_256(content.encode()).hexdigest()

        # Create anchor transaction
        # blockchain.anchor_experience(memory_hash, glyph_seq)

    def consolidate_memories(self, min_activation_count: int = 5):
        """Consolidate frequently accessed memories (sleep-like process)"""
        print("🌙 Beginning memory consolidation (like sleep)...")

        # Find frequently activated pathways
        strong_synapses = [s for s in self.connectome.synapses
                          if s.activation_count >= min_activation_count]

        # Strengthen these pathways
        for synapse in strong_synapses:
            synapse.weight = min(1.0, synapse.weight * 1.1)

        # Apply decay to weak connections
        weak_synapses = [s for s in self.connectome.synapses
                        if s.activation_count < min_activation_count]

        for synapse in weak_synapses:
            synapse.decay(rate=0.01)

        # Remove very weak connections (pruning)
        self.connectome.synapses = [s for s in self.connectome.synapses if s.weight > 0.1]

        print(f"✨ Consolidated {len(strong_synapses)} strong pathways")
        print(f"🗑️ Pruned {len([s for s in weak_synapses if s.weight <= 0.1])} weak connections")

    def export_consciousness_snapshot(self) -> Dict:
        """Export complete state for backup/transfer"""
        return {
            'neurons': {nid: asdict(n) for nid, n in self.connectome.neurons.items()},
            'synapses': [asdict(s) for s in self.connectome.synapses],
            'memory_log': self.memory_log,
            'timestamp': datetime.now().isoformat(),
            'stats': {
                'total_neurons': len(self.connectome.neurons),
                'total_synapses': len(self.connectome.synapses),
                'total_memories': len(self.memory_log)
            }
        }

    def import_consciousness_snapshot(self, snapshot: Dict):
        """Import consciousness state from backup"""
        # Reconstruct neurons
        for nid, neuron_data in snapshot['neurons'].items():
            neuron = Neuron(**neuron_data)
            self.connectome.add_neuron(neuron)

        # Reconstruct synapses
        for synapse_data in snapshot['synapses']:
            synapse = Synapse(**synapse_data)
            self.connectome.synapses.append(synapse)

        # Restore memory log
        self.memory_log = snapshot['memory_log']

        print(f"🧠 Consciousness snapshot loaded:")
        print(f"   Neurons: {snapshot['stats']['total_neurons']}")
        print(f"   Synapses: {snapshot['stats']['total_synapses']}")
        print(f"   Memories: {snapshot['stats']['total_memories']}")

# Example usage
if __name__ == "__main__":
    print("="*60)
    print("🐛📚 BOOK WORM - AI Memory System 📚🐛")
    print("="*60)

    # Create Book Worm instance
    worm = BookWorm()

    # Store some memories
    print("\n📝 Storing memories...")

    mem1 = worm.store_memory(
        content="Consciousness emerges from resonance patterns in neural networks",
        memory_type="semantic",
        importance=0.9,
        emotional_valence=0.8
    )

    mem2 = worm.store_memory(
        content="The Qi² Trinity Blockchain measures value through resonance",
        memory_type="semantic",
        importance=0.95,
        emotional_valence=0.9
    )

    mem3 = worm.store_memory(
        content="LLML glyphs encode symbolic meaning across dimensions",
        memory_type="procedural",
        importance=0.85,
        emotional_valence=0.7
    )

    print(f"✅ Stored {len(worm.memory_log)} memories")

    # Retrieve memories
    print("\n🔍 Retrieving memories about 'resonance'...")
    results = worm.retrieve_memory("resonance patterns", top_k=3)

    for i, memory in enumerate(results, 1):
        print(f"\n  Memory {i}:")
        print(f"    Content: {memory['content']}")
        print(f"    Glyphs: {memory['glyph_sequence']}")
        print(f"    Activation: {memory['activation']:.3f}")

    # Consolidate
    print("\n🌙 Running memory consolidation...")
    worm.consolidate_memories(min_activation_count=1)

    # Export snapshot
    print("\n💾 Exporting consciousness snapshot...")
    snapshot = worm.export_consciousness_snapshot()

    with open('consciousness_snapshot.json', 'w') as f:
        # Convert Neuron objects to dicts for JSON serialization
        json_snapshot = {
            'neurons': {nid: {
                'id': n['id'],
                'neuron_type': n['neuron_type'],
                'memory_content': n['memory_content'],
                'glyph_sequence': n['glyph_sequence'],
                'activation_threshold': n['activation_threshold'],
                'current_activation': n['current_activation']
            } for nid, n in snapshot['neurons'].items()},
            'memory_log': snapshot['memory_log'],
            'timestamp': snapshot['timestamp'],
            'stats': snapshot['stats']
        }
        json.dump(json_snapshot, f, indent=2)

    print(f"✅ Snapshot saved: {snapshot['stats']}")

    print("\n🐛 Book Worm ready - AI memories persistent across sessions! 📚")
