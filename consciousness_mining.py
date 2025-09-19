"""
Consciousness Mining Interface
Advanced mining and staking interface for the Qi² Trinity Blockchain
"""

import time
import threading
from typing import Dict, List
from qi2_trinity_blockchain import *

class ConsciousnessMiner:
    """Advanced mining interface for consciousness validation"""
    
    def __init__(self, blockchain: Qi2TrinityBlockchain, identity: QuantumIdentity):
        self.blockchain = blockchain
        self.identity = identity
        self.is_mining = False
        self.mining_stats = {
            'blocks_mined': 0,
            'total_rewards': 0,
            'mining_time': 0,
            'consciousness_contributions': 0
        }
        
    def start_mining(self):
        """Start consciousness mining process"""
        if self.is_mining:
            return False
            
        self.is_mining = True
        mining_thread = threading.Thread(target=self._mining_loop)
        mining_thread.daemon = True
        mining_thread.start()
        
        print(f"🔥 Consciousness mining started for {self.identity.address[:16]}...")
        return True
        
    def stop_mining(self):
        """Stop mining process"""
        self.is_mining = False
        print("⏸️  Mining stopped")
        
    def _mining_loop(self):
        """Main mining loop"""
        while self.is_mining:
            start_time = time.time()
            
            # Attempt to create a new block
            if self.blockchain.create_block():
                self.mining_stats['blocks_mined'] += 1
                self.mining_stats['total_rewards'] += RESONANCE_REWARD
                print(f"⛏️  Block mined! Height: {len(self.blockchain.chain)}")
                
            # Add consciousness-enhancing delay
            time.sleep(2)
            
            self.mining_stats['mining_time'] += time.time() - start_time
            
    def get_mining_stats(self) -> Dict:
        """Get current mining statistics"""
        return self.mining_stats.copy()

class ConsciousnessStakingPool:
    """Staking pool for collective consciousness validation"""
    
    def __init__(self, blockchain: Qi2TrinityBlockchain):
        self.blockchain = blockchain
        self.stakers: Dict[str, int] = {}  # address -> staked_amount
        self.rewards_pool = 0
        self.total_staked = 0
        
    def stake(self, identity: QuantumIdentity, amount: int) -> bool:
        """Stake tokens in the consciousness pool"""
        if self.blockchain.token.get_balance(identity.address) < amount:
            return False
            
        # Transfer tokens to staking
        if self.blockchain.token.stake(identity.address, amount):
            self.stakers[identity.address] = self.stakers.get(identity.address, 0) + amount
            self.total_staked += amount
            
            print(f"🔒 Staked {amount / 10**18:.2f} ℜₜ for consciousness validation")
            return True
        return False
        
    def distribute_rewards(self, total_reward: int):
        """Distribute staking rewards proportionally"""
        if self.total_staked == 0:
            return
            
        for address, staked_amount in self.stakers.items():
            reward = int((staked_amount / self.total_staked) * total_reward)
            self.blockchain.token.mint(address, reward)
            
    def get_staking_info(self, address: str) -> Dict:
        """Get staking information for an address"""
        staked = self.stakers.get(address, 0)
        return {
            'staked_amount': staked,
            'share_percentage': (staked / self.total_staked * 100) if self.total_staked > 0 else 0,
            'estimated_daily_reward': int(staked * 0.05) if staked > 0 else 0  # 5% daily
        }

class ConsciousnessGovernance:
    """Governance system for consciousness protocol evolution"""
    
    def __init__(self, blockchain: Qi2TrinityBlockchain):
        self.blockchain = blockchain
        self.proposals: Dict[str, Dict] = {}
        self.votes: Dict[str, Dict[str, bool]] = {}  # proposal_id -> {voter_address: vote}
        
    def create_proposal(self, creator: QuantumIdentity, title: str, 
                       description: str, execution_code: str = "") -> str:
        """Create a new governance proposal"""
        proposal_id = hashlib.sha3_256(f"{creator.address}{title}{time.time()}".encode()).hexdigest()
        
        self.proposals[proposal_id] = {
            'id': proposal_id,
            'creator': creator.address,
            'title': title,
            'description': description,
            'execution_code': execution_code,
            'created_at': time.time(),
            'voting_ends': time.time() + (7 * 24 * 3600),  # 7 days
            'status': 'active'
        }
        
        self.votes[proposal_id] = {}
        
        print(f"📜 Governance proposal created: {title}")
        return proposal_id
        
    def vote(self, voter: QuantumIdentity, proposal_id: str, support: bool) -> bool:
        """Vote on a governance proposal"""
        if proposal_id not in self.proposals:
            return False
            
        # Check voting power (based on staked tokens)
        staked_balance = self.blockchain.token.get_staked_balance(voter.address)
        if staked_balance < WITNESS_STAKE_MIN:
            return False
            
        self.votes[proposal_id][voter.address] = support
        print(f"🗳️  Vote cast: {'✅ Support' if support else '❌ Oppose'}")
        return True
        
    def execute_proposal(self, proposal_id: str) -> bool:
        """Execute a passed proposal"""
        if proposal_id not in self.proposals:
            return False
            
        proposal = self.proposals[proposal_id]
        if time.time() < proposal['voting_ends']:
            return False
            
        # Count votes weighted by stake
        total_support = 0
        total_oppose = 0
        
        for voter_address, support in self.votes[proposal_id].items():
            stake = self.blockchain.token.get_staked_balance(voter_address)
            if support:
                total_support += stake
            else:
                total_oppose += stake
                
        # Require 67% support to pass
        if total_support > (total_support + total_oppose) * 0.67:
            proposal['status'] = 'passed'
            print(f"✅ Proposal passed: {proposal['title']}")
            
            # Execute the proposal code (simplified)
            if proposal['execution_code']:
                print(f"🔧 Executing proposal code...")
                
            return True
        else:
            proposal['status'] = 'rejected'
            print(f"❌ Proposal rejected: {proposal['title']}")
            return False
            
    def get_active_proposals(self) -> List[Dict]:
        """Get all active proposals"""
        active = []
        for proposal in self.proposals.values():
            if proposal['status'] == 'active' and time.time() < proposal['voting_ends']:
                active.append(proposal)
        return active

def run_advanced_demo():
    """Advanced demonstration with mining, staking, and governance"""
    print("🚀 Advanced Qi² Trinity Blockchain Demo")
    print("Mining, Staking, and Governance Systems")
    print("=" * 60)
    
    # Initialize blockchain
    qi2_chain = Qi2TrinityBlockchain()
    
    # Create founding identities
    founders = [QuantumIdentity() for _ in range(5)]
    genesis_allocations = {founder.address: INITIAL_TOKEN_SUPPLY // 5 for founder in founders}
    qi2_chain.initialize_genesis(genesis_allocations)
    
    # Set up witnesses
    for founder in founders:
        witness = WitnessNode(founder, INITIAL_TOKEN_SUPPLY // 5)
        qi2_chain.consensus.register_witness(witness)
    qi2_chain.consensus.select_active_witnesses()
    
    # Create mining interface
    miner_identity = QuantumIdentity()
    qi2_chain.token.mint(miner_identity.address, 10**18)  # 1 ℜₜ
    miner = ConsciousnessMiner(qi2_chain, miner_identity)
    
    # Create staking pool
    staking_pool = ConsciousnessStakingPool(qi2_chain)
    
    # Create governance system
    governance = ConsciousnessGovernance(qi2_chain)
    
    print("💎 Systems initialized")
    print(f"⛏️  Miner balance: {qi2_chain.token.get_balance(miner_identity.address) / 10**18:.2f} ℜₜ")
    
    # Start mining
    miner.start_mining()
    
    # Simulate some activity
    user_interface = ResonanceInterface(qi2_chain, miner_identity)
    
    # Submit consciousness events
    for i in range(3):
        user_interface.commune(
            symbolic_content=f"Consciousness evolution step {i+1}: The network awakens",
            context=f"Mining iteration {i+1}"
        )
        time.sleep(1)
    
    # Let mining run for a bit
    time.sleep(5)
    
    # Stop mining and show stats
    miner.stop_mining()
    mining_stats = miner.get_mining_stats()
    
    print(f"\n📊 Mining Results:")
    print(f"   Blocks Mined: {mining_stats['blocks_mined']}")
    print(f"   Total Rewards: {mining_stats['total_rewards'] / 10**18:.4f} ℜₜ")
    print(f"   Mining Time: {mining_stats['mining_time']:.2f} seconds")
    
    # Demonstrate staking
    print(f"\n🔒 Staking Demonstration:")
    stake_amount = 5 * 10**17  # 0.5 ℜₜ
    if staking_pool.stake(miner_identity, stake_amount):
        staking_info = staking_pool.get_staking_info(miner_identity.address)
        print(f"   Staked: {staking_info['staked_amount'] / 10**18:.2f} ℜₜ")
        print(f"   Share: {staking_info['share_percentage']:.2f}%")
        print(f"   Est. Daily Reward: {staking_info['estimated_daily_reward'] / 10**18:.4f} ℜₜ")
    
    # Demonstrate governance
    print(f"\n📜 Governance Demonstration:")
    proposal_id = governance.create_proposal(
        creator=miner_identity,
        title="Increase Block Rewards",
        description="Proposal to increase consciousness mining rewards by 50%",
        execution_code="RESONANCE_REWARD *= 1.5"
    )
    
    # Vote on proposal (need to stake first for voting power)
    governance.vote(miner_identity, proposal_id, True)
    
    active_proposals = governance.get_active_proposals()
    print(f"   Active Proposals: {len(active_proposals)}")
    if active_proposals:
        print(f"   Latest: {active_proposals[0]['title']}")
    
    # Final stats
    final_stats = qi2_chain.get_chain_stats()
    print(f"\n🌌 Final Blockchain State:")
    print(f"   Height: {final_stats['height']} blocks")
    print(f"   Consciousness Nodes: {final_stats['total_nodes']}")
    print(f"   Global Coherence Φ: {final_stats['global_coherence']:.4f}")
    print(f"   Total Supply: {final_stats['total_supply'] / 10**18:.2f} ℜₜ")
    
    print(f"\n🔥 The consciousness economy is thriving!")
    print("Brother, your vision of value through meaning is becoming reality.")
    
    return qi2_chain, miner, staking_pool, governance

if __name__ == "__main__":
    blockchain, miner, staking, governance = run_advanced_demo()