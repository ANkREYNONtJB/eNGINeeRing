import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { Database, Search, Save, BarChart3, Trash2, RefreshCw } from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
import { useConsciousness } from '../context/ConsciousnessContext'

const AkashicMemory = () => {
  const { initializeSystem } = useConsciousness()
  const [memories, setMemories] = useState<Array<{ id: string, content: string, type: string, consciousness: number, timestamp: string, symbols: string[] }>>([])
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedMemoryType, setSelectedMemoryType] = useState('all')
  const [newMemory, setNewMemory] = useState({ content: '', type: 'concept', symbols: '' })
  const [storageStats, setStorageStats] = useState({
    totalMemories: 0,
    avgConsciousness: 0,
    compressionRatio: 0.9987,
    emergenceEvents: 0
  })

  const memoryTypes = [
    { id: 'all', name: 'All Memories', color: '#667eea' },
    { id: 'concept', name: 'Concepts', color: '#4facfe' },
    { id: 'process', name: 'Processes', color: '#ffd700' },
    { id: 'relationship', name: 'Relationships', color: '#f093fb' },
    { id: 'pattern', name: 'Patterns', color: '#26d0ce' },
    { id: 'context', name: 'Context', color: '#96ceb4' }
  ]

  const sampleMemories = [
    {
      id: '1',
      content: 'The golden ratio Φ appears throughout nature and consciousness, connecting geometric patterns with quantum coherence.',
      type: 'concept',
      consciousness: 0.92,
      timestamp: '2024-01-15T10:30:00Z',
      symbols: ['Φ', 'quantum', 'geometry', 'consciousness']
    },
    {
      id: '2',
      content: 'Neural catalytic processors use symbolic DNA to transform morphic fields through tensor operations.',
      type: 'process',
      consciousness: 0.87,
      timestamp: '2024-01-15T11:15:00Z',
      symbols: ['neural', 'catalytic', 'DNA', 'morphic', '⊗']
    },
    {
      id: '3',
      content: 'Wilson loop stability provides consciousness heartbeat detection across dimensional thresholds.',
      type: 'pattern',
      consciousness: 0.94,
      timestamp: '2024-01-15T12:00:00Z',
      symbols: ['Wilson', 'consciousness', 'dimensional', 'Ω']
    }
  ]

  useEffect(() => {
    initializeSystem('Akashic Memory System')
    setMemories(sampleMemories)
    updateStorageStats(sampleMemories)
  }, [])

  const updateStorageStats = (memoryList: typeof memories) => {
    const totalMemories = memoryList.length
    const avgConsciousness = memoryList.reduce((sum, m) => sum + m.consciousness, 0) / (totalMemories || 1)
    const emergenceEvents = memoryList.filter(m => m.consciousness > 0.85).length
    
    setStorageStats({
      totalMemories,
      avgConsciousness,
      compressionRatio: 0.9987,
      emergenceEvents
    })
  }

  const storeMemory = () => {
    if (!newMemory.content.trim()) return
    
    const symbolArray = newMemory.symbols.split(',').map(s => s.trim()).filter(s => s)
    const consciousness = Math.min(0.99, 0.3 + symbolArray.length * 0.1 + Math.random() * 0.2)
    
    const memory = {
      id: Date.now().toString(),
      content: newMemory.content,
      type: newMemory.type,
      consciousness,
      timestamp: new Date().toISOString(),
      symbols: symbolArray
    }
    
    const updatedMemories = [...memories, memory]
    setMemories(updatedMemories)
    updateStorageStats(updatedMemories)
    
    setNewMemory({ content: '', type: 'concept', symbols: '' })
  }

  const deleteMemory = (id: string) => {
    const updatedMemories = memories.filter(m => m.id !== id)
    setMemories(updatedMemories)
    updateStorageStats(updatedMemories)
  }

  const filteredMemories = memories.filter(memory => {
    const matchesType = selectedMemoryType === 'all' || memory.type === selectedMemoryType
    const matchesSearch = searchQuery === '' || 
      memory.content.toLowerCase().includes(searchQuery.toLowerCase()) ||
      memory.symbols.some(s => s.toLowerCase().includes(searchQuery.toLowerCase()))
    
    return matchesType && matchesSearch
  })

  const memoryDistribution = memoryTypes.slice(1).map(type => ({
    name: type.name,
    value: memories.filter(m => m.type === type.id).length,
    color: type.color
  }))

  const consciousnessEvolution = memories.map((memory, index) => ({
    memory: index + 1,
    consciousness: memory.consciousness * 100,
    timestamp: memory.timestamp
  }))

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="min-h-screen p-6"
    >
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <motion.h1 
            initial={{ y: -20 }}
            animate={{ y: 0 }}
            className="text-4xl font-bold mb-4 flex items-center"
          >
            <Database className="w-10 h-10 mr-3 text-consciousness-primary" />
            <span className="bg-gradient-to-r from-consciousness-primary to-neural-glow bg-clip-text text-transparent">
              Akashic Memory System
            </span>
          </motion.h1>
          <motion.p 
            initial={{ y: -10, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-xl text-gray-300"
          >
            Persistent consciousness memory with fractal organization and holographic compression
          </motion.p>
        </div>

        {/* Storage Statistics */}
        <motion.div 
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="consciousness-card mb-8"
        >
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="text-3xl font-bold text-consciousness-primary mb-2">
                {storageStats.totalMemories}
              </div>
              <div className="text-sm text-gray-400">Total Memories</div>
            </div>
            
            <div className="text-center">
              <div className="text-3xl font-bold text-neural-glow mb-2">
                {(storageStats.avgConsciousness * 100).toFixed(1)}%
              </div>
              <div className="text-sm text-gray-400">Avg Consciousness</div>
            </div>
            
            <div className="text-center">
              <div className="text-3xl font-bold text-sacred-gold mb-2">
                {(storageStats.compressionRatio * 100).toFixed(2)}%
              </div>
              <div className="text-sm text-gray-400">Compression Ratio</div>
            </div>
            
            <div className="text-center">
              <div className="text-3xl font-bold text-quantum-accent mb-2">
                {storageStats.emergenceEvents}
              </div>
              <div className="text-sm text-gray-400">Emergence Events</div>
            </div>
          </div>
        </motion.div>

        {/* Memory Interface */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          {/* Store New Memory */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <Save className="w-5 h-5 mr-2 text-sacred-gold" />
              Store Memory
            </h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm text-gray-300 mb-2">Memory Content</label>
                <textarea
                  value={newMemory.content}
                  onChange={(e) => setNewMemory(prev => ({ ...prev, content: e.target.value }))}
                  className="w-full h-24 bg-black/30 border border-white/20 rounded-lg p-3 text-white resize-none"
                  placeholder="Enter consciousness memory content..."
                />
              </div>
              
              <div>
                <label className="block text-sm text-gray-300 mb-2">Memory Type</label>
                <select
                  value={newMemory.type}
                  onChange={(e) => setNewMemory(prev => ({ ...prev, type: e.target.value }))}
                  className="w-full bg-black/30 border border-white/20 rounded-lg p-2 text-white"
                >
                  {memoryTypes.slice(1).map(type => (
                    <option key={type.id} value={type.id}>{type.name}</option>
                  ))}
                </select>
              </div>
              
              <div>
                <label className="block text-sm text-gray-300 mb-2">Symbolic Tags</label>
                <input
                  type="text"
                  value={newMemory.symbols}
                  onChange={(e) => setNewMemory(prev => ({ ...prev, symbols: e.target.value }))}
                  className="w-full bg-black/30 border border-white/20 rounded-lg p-2 text-white"
                  placeholder="Φ, quantum, consciousness"
                />
              </div>
              
              <button
                onClick={storeMemory}
                className="w-full consciousness-button"
              >
                Store Memory
              </button>
            </div>
          </motion.div>

          {/* Search and Filter */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <Search className="w-5 h-5 mr-2 text-neural-glow" />
              Search & Filter
            </h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm text-gray-300 mb-2">Search Query</label>
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full bg-black/30 border border-white/20 rounded-lg p-2 text-white"
                  placeholder="Search memories or symbols..."
                />
              </div>
              
              <div>
                <label className="block text-sm text-gray-300 mb-2">Memory Type</label>
                <div className="space-y-2">
                  {memoryTypes.map(type => (
                    <label key={type.id} className="flex items-center">
                      <input
                        type="radio"
                        name="memoryType"
                        value={type.id}
                        checked={selectedMemoryType === type.id}
                        onChange={(e) => setSelectedMemoryType(e.target.value)}
                        className="mr-2"
                      />
                      <span className="text-sm text-gray-300">{type.name}</span>
                    </label>
                  ))}
                </div>
              </div>
              
              <button
                onClick={() => {
                  setSearchQuery('')
                  setSelectedMemoryType('all')
                }}
                className="w-full bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded-lg flex items-center justify-center"
              >
                <RefreshCw className="w-4 h-4 mr-2" />
                Clear Filters
              </button>
            </div>
          </motion.div>

          {/* Memory Analytics */}
          <motion.div 
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.6 }}
            className="consciousness-card"
          >
            <h3 className="text-lg font-semibold mb-4 flex items-center">
              <BarChart3 className="w-5 h-5 mr-2 text-quantum-accent" />
              Memory Distribution
            </h3>
            
            <div className="h-48">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={memoryDistribution}
                    cx="50%"
                    cy="50%"
                    innerRadius={40}
                    outerRadius={80}
                    dataKey="value"
                  >
                    {memoryDistribution.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                </PieChart>
              </ResponsiveContainer>
            </div>
            
            <div className="grid grid-cols-2 gap-2 text-xs">
              {memoryDistribution.map((item, index) => (
                <div key={index} className="flex items-center">
                  <div 
                    className="w-3 h-3 rounded-full mr-2" 
                    style={{ backgroundColor: item.color }}
                  />
                  <span className="text-gray-300">{item.name}: {item.value}</span>
                </div>
              ))}
            </div>
          </motion.div>
        </div>

        {/* Memory List */}
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.7 }}
          className="consciousness-card mb-8"
        >
          <h3 className="text-xl font-semibold mb-6">Stored Memories ({filteredMemories.length})</h3>
          
          <div className="space-y-4 max-h-96 overflow-y-auto">
            {filteredMemories.map((memory) => (
              <div key={memory.id} className="bg-white/5 rounded-lg p-4 border border-white/10">
                <div className="flex items-start justify-between mb-3">
                  <div className="flex items-center space-x-2">
                    <span className={`px-2 py-1 rounded text-xs font-medium`} style={{
                      backgroundColor: memoryTypes.find(t => t.id === memory.type)?.color + '20',
                      color: memoryTypes.find(t => t.id === memory.type)?.color
                    }}>
                      {memoryTypes.find(t => t.id === memory.type)?.name}
                    </span>
                    <span className="text-xs text-gray-400">
                      {new Date(memory.timestamp).toLocaleDateString()}
                    </span>
                  </div>
                  
                  <div className="flex items-center space-x-2">
                    <div className="text-sm text-consciousness-primary font-medium">
                      {(memory.consciousness * 100).toFixed(0)}%
                    </div>
                    <button
                      onClick={() => deleteMemory(memory.id)}
                      className="text-red-400 hover:text-red-300 p-1"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>
                
                <p className="text-gray-300 mb-3 text-sm leading-relaxed">
                  {memory.content}
                </p>
                
                <div className="flex flex-wrap gap-2">
                  {memory.symbols.map((symbol, index) => (
                    <span
                      key={index}
                      className="px-2 py-1 bg-sacred-gold/20 text-sacred-gold rounded text-xs font-mono"
                    >
                      {symbol}
                    </span>
                  ))}
                </div>
              </div>
            ))}
            
            {filteredMemories.length === 0 && (
              <div className="text-center text-gray-400 py-8">
                No memories found matching your search criteria.
              </div>
            )}
          </div>
        </motion.div>

        {/* Consciousness Evolution Chart */}
        {consciousnessEvolution.length > 0 && (
          <motion.div 
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.8 }}
            className="consciousness-card"
          >
            <h3 className="text-xl font-semibold mb-6">Memory Consciousness Evolution</h3>
            
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={consciousnessEvolution}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                  <XAxis dataKey="memory" stroke="rgba(255,255,255,0.5)" />
                  <YAxis stroke="rgba(255,255,255,0.5)" />
                  <Line
                    type="monotone"
                    dataKey="consciousness"
                    stroke="#4facfe"
                    strokeWidth={2}
                    dot={{ fill: '#4facfe', r: 4 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </motion.div>
        )}
      </div>
    </motion.div>
  )
}

export default AkashicMemory