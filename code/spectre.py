import sys
import random
import numpy as np

# Takes slope, y-int and determines if the point is above or below the random line.
def above_or_below(point, m, b):
    if(point[0] > m*point[1] + b):
        return "1" # Above the line
    else:
        return "0" # Below the line
        
def b(points,m): # Returns the y-intercept
    b = points[3] - (m*points[1])
    
    return b

def slope(points): # Returns the slope of the random line
    m = (points[1]-points[0])/ (points[3]-points[2]);
    
    return m

def centroid(spectrum): # Returns the centroid of all the peaks of a spectrum as an (x,y) pair
    mToZ = 0.0
    intensity = 0.0
    length = len(spectrum)
    
    for spectre in spectrum:
        intensity+=float(spectre[0])
        mToZ+=float(spectre[1])
    intensity = intensity / length
    mToZ = mToZ / length
    
    return [intensity,mToZ]


def max_val(vector, pos): # Calculates the max values for generating the random line
       maxV = 0
       for vec in vector:
              if(vec[pos] > maxV):
                     maxV = float(vec[pos])
       return maxV

def unit_vector(vector): # Unit vector function I may have used
       magnitude = np.sqrt((float(vector[0])**2)+(float(vector[1])**2))
       return [float(vector[0])/magnitude, float(vector[1])/magnitude]

def random_vector(x_max,y_max): # Returns two random points in the plane that will define the random vector
       rand_x1 = random.uniform(0,x_max)
       rand_y1 = random.uniform(0,y_max)
       rand_x2 = random.uniform(0,x_max)
       rand_y2 = random.uniform(0,y_max)

       rand_vec = [rand_x1,rand_x2,rand_y1,rand_y2]

       return rand_vec

def main(argv):

    if(len(argv) != 1):
        print("Usage spectre.py <.mgf filename>")
    else:

        spectre = [] # Temporary list that will hold the spectre as they are read in
        
        final_spectre = [] # Will hold the centroid of each individiual spectrum
        
        hashes = [] # Will hold the hashes of the final_spectre for printing the clusters at the end
        
        # Open the file for reading
        f = open(argv[0], 'r+')
        for line in f:
            line = line.replace("\n", "")
            line = line.split(" ")
                  
            try:   # Is data, append it to the spectre
                float(line[0])
                spectre.append(line)
            except: # Check if it's the END of the spectrum, if so clear the temp list and calculate that spectrum's centroid
                if(line[0] == "END"):
                    final_spectre.append(centroid(spectre))
                    spectre = []


           

        x_max = max_val(final_spectre,0) # Get's the max x value of the final_spectre
        
        y_max = max_val(final_spectre,1) # Get's the max y value of all the final_spectre
        
           
           # Set the hashes to be appended to
        for x in range(0,len(final_spectre)):
            hashes.append("")
        
        # 10x get a random vector, calculate b, m and hash for each final_spectre
        for x in range(0,10):
            
            rand_vec = random_vector(x_max, y_max)
            
            b_val = (b(rand_vec, m_val))
            
            m_val = slope(rand_vec)
            
            for i in range(0,len(final_spectre)):
            
                hashes[i]+=(above_or_below(final_spectre[i], m_val, b_val))
        
        
        # Get all unique hashes
        unique_hashes = []
        for hash in hashes:
            if(hash not in unique_hashes):
                unique_hashes.append(hash)
        
        #Print the clusters
        output_string = "";
        for hash in unique_hashes:
            for x in range(0,len(final_spectre)):
                if(hashes[x] == hash):
                    output_string += str(x) + " "
            print(output_string)
            output_string = ""
        
            
if __name__=='__main__':
       main(sys.argv[1:])
