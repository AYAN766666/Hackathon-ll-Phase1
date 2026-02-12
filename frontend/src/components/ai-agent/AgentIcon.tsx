import React, { useState } from 'react';

interface AgentIconProps {
  onClick: () => void;
  isOpen: boolean;
}

const AgentIcon: React.FC<AgentIconProps> = ({ onClick, isOpen }) => {
  const [hovered, setHovered] = useState(false);

  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={`
        fixed bottom-6 right-6 z-50
        w-14 h-14 rounded-full flex items-center justify-center
        bg-blue-600 hover:bg-blue-700
        text-white shadow-lg
        transform transition-all duration-200
        ${isOpen ? 'bg-blue-800 scale-110' : ''}
        ${hovered ? 'scale-110' : 'scale-100'}
      `}
      aria-label={isOpen ? "Close AI Agent" : "Open AI Agent"}
    >
      <div className="relative">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          className="fill-current"
        >
          <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1H5C3.89 1 3 1.89 3 3V7H1V9H3V14C3 17.31 5.69 20 9 20S15 17.31 15 14V9H21ZM11 9H5V4H11V9ZM5 15V14H9C9.55 14 10 14.45 10 15S9.55 16 9 16H5Z"/>
        </svg>
        {isOpen && (
          <div className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 rounded-full flex items-center justify-center">
            <span className="text-xs text-white">!</span>
          </div>
        )}
      </div>
    </button>
  );
};

export default AgentIcon;