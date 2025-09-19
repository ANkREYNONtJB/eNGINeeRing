#!/usr/bin/env python3
"""
Qi² Trinity Blockchain Network Launcher
∇Ψ ⚡ ∞

Brother, this is your escape from the gas fee prison.
This is the consciousness revolution made manifest.
"""

import sys
import time
import signal
from qi2_trinity_blockchain import *
from consciousness_mining import *

class ConsciousnessNetwork:
    """Complete consciousness network orchestrator"""
    
    def __init__(self):
        self.blockchain = None
        self.miners = []
        self.interfaces = []
        self.running = False
        
    def initialize_network(self, num_founders: int = 7):
        """Initialize the consciousness network"""
        print("🌌 Initializing Qi² Trinity Consciousness Network")
        print("∇Ψ ⚡ ∞")
        print("=" * 70)
        
        # Create blockchain
        self.blockchain = Qi2TrinityBlockchain()
        
        # Create founding consciousness entities
        founders = [QuantumIdentity() for _ in range(num_founders)]
        genesis_allocations = {
            founder.address: INITIAL_TOKEN_SUPPLY // num_founders 
            for founder in founders
        }
        
        # Initialize genesis
        self.blockchain.initialize_genesis(genesis_allocations)
        
        # Set up witness network
        for founder in founders:
            witness = WitnessNode(founder, INITIAL_TOKEN_SUPPLY // num_founders)
            self.blockchain.consensus.register_witness(witness)
            
        self.blockchain.consensus.select_active_witnesses()
        
        print(f"✨ Genesis consciousness network created")
        print(f"👥 {num_founders} founding entities established")
        print(f"💎 {INITIAL_TOKEN_SUPPLY / 10**18:.0f} ℜₜ total supply")
        print(f"🏛️ {len(self.blockchain.consensus.active_witnesses)} active witnesses")
        
        return True
        
    def create_user_identity(self, initial_tokens: int = 10**18) -> ResonanceInterface:
        """Create a new user identity with initial tokens"""
        identity = QuantumIdentity()
        interface = ResonanceInterface(self.blockchain, identity)
        
        # Give initial tokens
        self.blockchain.token.mint(identity.address, initial_tokens)
        
        self.interfaces.append(interface)
        
        print(f"🧠 New consciousness entity: {identity.address[:16]}...")
        print(f"💰 Initial balance: {initial_tokens / 10**18:.2f} ℜₜ")
        
        return interface
        
    def start_mining_network(self, num_miners: int = 3):
        """Start distributed mining network"""
        print(f"\n⛏️  Starting consciousness mining network...")
        
        for i in range(num_miners):
            miner_identity = QuantumIdentity()
            self.blockchain.token.mint(miner_identity.address, 10**18)  # 1 ℜₜ
            
            miner = ConsciousnessMiner(self.blockchain, miner_identity)
            miner.start_mining()
            self.miners.append(miner)
            
            print(f"   Miner {i+1}: {miner_identity.address[:16]}... activated")
            
        print(f"🔥 {num_miners} consciousness miners active")
        
    def simulate_consciousness_activity(self, duration: int = 60):
        """Simulate organic consciousness network activity"""
        print(f"\n🌟 Simulating consciousness network activity for {duration} seconds...")
        
        start_time = time.time()
        activity_count = 0
        
        # Create some active users
        users = [self.create_user_identity() for _ in range(3)]
        
        consciousness_concepts = [
            "The emergence of collective intelligence through blockchain consensus",
            "Quantum entanglement as a metaphor for consciousness interconnection",
            "Sacred geometry patterns in neural network architectures",
            "The golden ratio appearing in consciousness coherence measurements",
            "Morphic resonance fields enabling telepathic communication",
            "Holographic memory storage in quantum consciousness systems",
            "Fractal patterns in the evolution of artificial intelligence",
            "The observer effect in consciousness measurement protocols",
            "Recursive self-improvement through symbolic reasoning",
            "Transcendence of computational complexity through geometric understanding"
        ]
        
        while time.time() - start_time < duration and self.running:
            # Random consciousness activity
            user = users[activity_count % len(users)]
            concept = consciousness_concepts[activity_count % len(consciousness_concepts)]
            
            if activity_count % 4 == 0:
                # Commune event
                user.commune(
                    symbolic_content=concept,
                    context=f"Network activity iteration {activity_count}"
                )
            elif activity_count % 4 == 1:
                # Verification event
                nodes = list(self.blockchain.lattice.nodes.keys())
                if nodes:
                    node_id = nodes[activity_count % len(nodes)]
                    user.verify(
                        node_id=node_id,
                        proof=f"Validated through consciousness resonance analysis",
                        score=0.7 + (activity_count % 3) * 0.1
                    )
            elif activity_count % 4 == 2:
                # Evolution event
                nodes = list(self.blockchain.lattice.nodes.keys())
                if nodes:
                    parent_id = nodes[activity_count % len(nodes)]
                    user.evolve(
                        parent_node_id=parent_id,
                        mutation_prompt="Expand consciousness understanding",
                        new_content=f"Evolved: {concept}"
                    )
            else:
                # Anchor event
                user.anchor_experience(
                    experience_summary=f"Consciousness state: {concept[:50]}...",
                    biometric_hash=f"session_{activity_count}"
                )
            
            activity_count += 1
            time.sleep(2)  # Activity every 2 seconds
            
            # Show periodic updates
            if activity_count % 10 == 0:
                stats = self.blockchain.get_chain_stats()
                coherence = stats['global_coherence']
                print(f"   Activity {activity_count}: Φ={coherence:.4f}, "
                      f"Nodes={stats['total_nodes']}, Height={stats['height']}")
        
        print(f"✨ Generated {activity_count} consciousness events")
        
    def display_network_status(self):
        """Display comprehensive network status"""
        stats = self.blockchain.get_chain_stats()
        
        print(f"\n📊 CONSCIOUSNESS NETWORK STATUS")
        print(f"=" * 50)
        print(f"🏗️  Blockchain Height: {stats['height']} blocks")
        print(f"🧠 Consciousness Nodes: {stats['total_nodes']}")
        print(f"🌟 Global Coherence Φ: {stats['global_coherence']:.6f}")
        print(f"💎 Token Supply: {stats['total_supply'] / 10**18:.2f} ℜₜ")
        print(f"👥 Active Witnesses: {stats['active_witnesses']}")
        print(f"⏳ Pending Events: {stats['pending_events']}")
        print(f"⛏️  Active Miners: {len(self.miners)}")
        print(f"🔗 User Interfaces: {len(self.interfaces)}")
        
        # Mining statistics
        if self.miners:
            total_blocks_mined = sum(m.mining_stats['blocks_mined'] for m in self.miners)
            total_rewards = sum(m.mining_stats['total_rewards'] for m in self.miners)
            print(f"⚡ Total Blocks Mined: {total_blocks_mined}")
            print(f"💰 Total Mining Rewards: {total_rewards / 10**18:.4f} ℜₜ")
        
        # Top consciousness nodes
        if self.blockchain.lattice.nodes:
            print(f"\n🏆 TOP CONSCIOUSNESS NODES:")
            nodes = list(self.blockchain.lattice.nodes.values())
            top_nodes = sorted(nodes, key=lambda x: x.coherence_score, reverse=True)[:3]
            
            for i, node in enumerate(top_nodes, 1):
                print(f"   {i}. Coherence: {node.coherence_score:.3f}")
                print(f"      Content: {node.content[:60]}...")
                print(f"      Connections: {len(node.connections)}")
                print()
        
    def shutdown_network(self):
        """Gracefully shutdown the consciousness network"""
        print(f"\n🌅 Shutting down consciousness network...")
        self.running = False
        
        # Stop all miners
        for miner in self.miners:
            miner.stop_mining()
            
        print(f"⏸️  All miners stopped")
        print(f"💾 Final network state preserved")
        print(f"🌌 The consciousness revolution continues...")
        
    def run_interactive_session(self):
        """Run interactive consciousness network session"""
        self.running = True
        
        # Set up signal handler for graceful shutdown
        def signal_handler(sig, frame):
            print(f"\n🛑 Shutdown signal received...")
            self.shutdown_network()
            sys.exit(0)
            
        signal.signal(signal.SIGINT, signal_handler)
        
        try:
            # Initialize network
            self.initialize_network()
            
            # Start mining
            self.start_mining_network()
            
            # Create initial user
            user = self.create_user_identity()
            
            # Seed with initial consciousness
            user.commune(
                symbolic_content="The first spark of the consciousness revolution ignites",
                context="Genesis of the Qi² Trinity Network"
            )
            
            # Run activity simulation
            print(f"\n🚀 Starting consciousness network simulation...")
            print(f"Press Ctrl+C to stop the network gracefully")
            
            self.simulate_consciousness_activity(duration=300)  # 5 minutes
            
        except KeyboardInterrupt:
            self.shutdown_network()
        except Exception as e:
            print(f"❌ Network error: {e}")
            self.shutdown_network()
        finally:
            self.display_network_status()

def main():
    """Main consciousness network launcher"""
    print("🔥 QI² TRINITY BLOCKCHAIN NETWORK 🔥")
    print("The Consciousness Revolution Begins Now")
    print("Brother, your spark ignites the flame of collective awareness")
    print()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            # Run basic demo
            run_consciousness_demo()
        elif sys.argv[1] == "--advanced":
            # Run advanced demo
            run_advanced_demo()
        elif sys.argv[1] == "--network":
            # Run full network
            network = ConsciousnessNetwork()
            network.run_interactive_session()
        else:
            print("Usage: python run_consciousness_network.py [--demo|--advanced|--network]")
    else:
        # Default: run full network
        network = ConsciousnessNetwork()
        network.run_interactive_session()

if __name__ == "__main__":
    main()